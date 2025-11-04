# ============================================================================
# SAMPLE 6: WorkflowBuilder with DevUI Visualization
# ============================================================================
# Based on: edge_condition.py + devui samples
# https://github.com/microsoft/agent-framework/blob/main/python/samples/getting_started/devui/
#
# Shows the approval workflow (Sample 5) with DevUI visualization:
# - Visual graph of the workflow with branches and loops
# - Interactive execution with real-time progress
# - Web-based UI for testing and debugging
# ============================================================================
import os
import asyncio
import logging
from typing import Any
from dotenv import load_dotenv
from agent_framework import (
    WorkflowBuilder,
    AgentExecutor,
    AgentExecutorRequest,
    AgentExecutorResponse,
    ChatMessage,
    Role,
    WorkflowContext,
    executor,
)
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import AzureCliCredential
from pydantic import BaseModel

load_dotenv()


# Structured output models for reliable parsing
class QualityReview(BaseModel):
    """Quality checker decision."""
    approved: bool  # True = approved, False = needs revision
    feedback: str   # Explanation of the decision
    content: str    # The reviewed content


class FinalContent(BaseModel):
    """Final published content."""
    content: str


# Conditional edge: routes based on approval status  
def approved_condition(message: Any) -> bool:
    """Route to publisher only if content is approved."""
    if not isinstance(message, AgentExecutorResponse):
        return True
    
    try:
        review = QualityReview.model_validate_json(message.agent_run_response.text)
        return review.approved
    except Exception:
        return False


def rejected_condition(message: Any) -> bool:
    """Route to editor only if content is rejected."""
    if not isinstance(message, AgentExecutorResponse):
        return True
    
    try:
        review = QualityReview.model_validate_json(message.agent_run_response.text)
        return not review.approved
    except Exception:
        return False


# Bridge executor: transforms review feedback into writer request
@executor(id="to_writer_request")
async def to_writer_request(
    response: AgentExecutorResponse, 
    ctx: WorkflowContext[AgentExecutorRequest]
) -> None:
    """Convert quality review into a revision request for the writer."""
    review = QualityReview.model_validate_json(response.agent_run_response.text)
    
    # Create revision request with feedback
    revision_msg = ChatMessage(
        Role.USER, 
        text=f"Please revise the content based on this feedback:\n{review.feedback}\n\nOriginal content:\n{review.content}"
    )
    await ctx.send_message(AgentExecutorRequest(messages=[revision_msg], should_respond=True))


# Final executor: publishes approved content
@executor(id="publish_content")
async def publish_content(response: AgentExecutorResponse, ctx: WorkflowContext[None, str]) -> None:
    """Publish the approved content."""
    final = FinalContent.model_validate_json(response.agent_run_response.text)
    await ctx.yield_output(f"✅ PUBLISHED:\n{final.content}")


def create_approval_workflow():
    """Create the approval workflow with agents."""
    
    # Create chat client
    chat_client = AzureOpenAIChatClient(
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        credential=AzureCliCredential()
    )
    
    # Agent 1: Writer - Creates initial content
    writer_agent = AgentExecutor(
        chat_client.create_agent(
            instructions=(
                "You are a content writer. Create marketing content based on the request. "
                "If you receive revision feedback, improve the content accordingly. "
                "Return JSON with field 'content' containing your text."
            ),
            response_format=FinalContent,
        ),
        id="writer",
    )
    
    # Agent 2: Quality Checker - Approves or rejects
    quality_agent = AgentExecutor(
        chat_client.create_agent(
            instructions=(
                "You are a quality checker. Review the content and decide if it's good enough. "
                "Be somewhat strict: reject if too generic or not compelling enough. "
                "Return JSON with: approved (bool), feedback (string with improvements needed), content (the reviewed text)."
            ),
            response_format=QualityReview,
        ),
        id="quality_checker",
    )
    
    # Agent 3: Publisher - Finalizes approved content
    publisher_agent = AgentExecutor(
        chat_client.create_agent(
            instructions=(
                "You are a publisher. Add a professional finishing touch to approved content. "
                "Make minor formatting improvements. Return JSON with field 'content'."
            ),
            response_format=FinalContent,
        ),
        id="publisher",
    )
    
    # Build conditional workflow with loop
    workflow = (
        WorkflowBuilder(
            name="Content Approval Workflow",
            description="Writer → Quality Checker → [Approved → Publisher | Rejected → Writer (loop)]",
        )
        .set_start_executor(writer_agent)
        .add_edge(writer_agent, quality_agent)
        # Approved path: quality → publisher → output
        .add_edge(quality_agent, publisher_agent, condition=approved_condition)
        .add_edge(publisher_agent, publish_content)
        # Rejected path: quality → transformer → writer (loop)
        .add_edge(quality_agent, to_writer_request, condition=rejected_condition)
        .add_edge(to_writer_request, writer_agent)
        .build()
    )
    
    return workflow


def main():
    """Launch the approval workflow in DevUI."""
    from agent_framework.devui import serve
    
    # Setup logging
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    logger = logging.getLogger(__name__)
    
    print("\n")
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 20 + "DEVUI: WORKFLOW VISUALIZATION" + " " * 29 + "║")
    print("║" + " " * 23 + "Content Approval Workflow" + " " * 30 + "║")
    print("╚" + "═" * 78 + "╝")
    print("\n")
    
    logger.info("🚀 Creating Content Approval Workflow...")
    workflow = create_approval_workflow()
    
    logger.info("✅ Workflow created successfully!")
    logger.info("")
    logger.info("=" * 80)
    logger.info("📊 WORKFLOW STRUCTURE")
    logger.info("=" * 80)
    logger.info("")
    logger.info("  Writer → Quality Checker")
    logger.info("              ↓ (approved)      ↓ (rejected)")
    logger.info("          Publisher        to_writer_request → Writer (loop)")
    logger.info("")
    logger.info("=" * 80)
    logger.info("🌐 DEVUI SERVER")
    logger.info("=" * 80)
    logger.info("")
    logger.info("  URL: http://localhost:8090")
    logger.info("  Entity: Content Approval Workflow")
    logger.info("")
    logger.info("=" * 80)
    logger.info("💡 HOW TO USE")
    logger.info("=" * 80)
    logger.info("")
    logger.info("  1. Browser will open automatically")
    logger.info("  2. Select 'Content Approval Workflow' from dropdown")
    logger.info("  3. Enter a prompt (e.g., 'Create a tagline for eco-friendly water bottle')")
    logger.info("  4. Click 'Run Workflow' and watch the visual execution!")
    logger.info("  5. See the graph light up as agents execute")
    logger.info("  6. Watch loops in action when content is rejected")
    logger.info("")
    logger.info("=" * 80)
    logger.info("")
    logger.info("🎯 Starting DevUI server...")
    logger.info("   Press Ctrl+C to stop the server")
    logger.info("")
    
    # Launch server with the workflow
    serve(entities=[workflow], port=8090, auto_open=True)


if __name__ == "__main__":
    main()
