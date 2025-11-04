# ============================================================================
# SAMPLE 5: WorkflowBuilder - Conditional Branching & Loops
# ============================================================================
# Based on: edge_condition.py, simple_loop.py
# https://github.com/microsoft/agent-framework/blob/main/python/samples/getting_started/workflows/control-flow/edge_condition.py
#
# WorkflowBuilder with conditional routing demonstrates:
# - Branching based on agent decisions (approved/rejected)
# - Loops for iterative improvements
# - Complex graph-based workflows
# ============================================================================
import os
import asyncio
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


# Counter to track iterations
class WorkflowState:
    writer_iteration = 0


# Conditional edge: routes based on approval status  
def approved_condition(message: Any) -> bool:
    """Route to publisher only if content is approved."""
    if not isinstance(message, AgentExecutorResponse):
        return True
    
    try:
        review = QualityReview.model_validate_json(message.agent_run_response.text)
        
        if review.approved:
            # Show quality checker decision ONLY when approved
            print(f"\n🔍 Quality Checker Review:")
            print(f"   Content: \"{review.content[:70]}...\"")
            print(f"   Decision: ✅ APPROVED - Routing to Publisher")
            return True
        else:
            return False
    except Exception:
        return False


def rejected_condition(message: Any) -> bool:
    """Route to editor only if content is rejected."""
    if not isinstance(message, AgentExecutorResponse):
        return True
    
    try:
        review = QualityReview.model_validate_json(message.agent_run_response.text)
        
        if not review.approved:
            # Show quality checker decision ONLY when rejected
            print(f"\n🔍 Quality Checker Review:")
            print(f"   Content: \"{review.content[:70]}...\"")
            print(f"   Decision: ❌ REJECTED")
            print(f"   Reason: {review.feedback}")
            return True
        else:
            return False
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
    
    # Track iterations
    WorkflowState.writer_iteration += 1
    
    # Show loop back
    print(f"\n🔄 Routing: REJECTED → Sending back to Writer for revision")
    print(f"   Feedback to writer: {review.feedback}")
    print("-" * 80)
    print(f"\n📝 Writer: Revising content (Iteration {WorkflowState.writer_iteration + 1})...")
    
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
    print(f"\n📤 Routing: APPROVED → Sending to Publisher")
    print("-" * 80)
    await ctx.yield_output(f"✅ PUBLISHED:\n{final.content}")


async def main():
    """
    Demonstrates conditional branching with approval workflow.
    
    Flow: 
      User Request → Writer → Quality Checker
                                    ↓
                              [if approved] → Publisher → Output
                              [if rejected] → Editor → Writer (loop back)
    
    This shows WorkflowBuilder's unique power:
    - Conditional routing based on agent decisions
    - Loops for iterative improvement
    - Complex graph structures
    """
    print("\n")
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 20 + "WORKFLOWBUILDER: CONDITIONAL BRANCHING" + " " * 20 + "║")
    print("║" + " " * 25 + "Approval Workflow Example" + " " * 28 + "║")
    print("╚" + "═" * 78 + "╝")
    print("\n")
    
    # Create chat client
    chat_client = AzureOpenAIChatClient(
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        credential=AzureCliCredential()
    )
    
    print("Creating specialized agents for approval workflow...")
    print("-" * 80)
    
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
                "You are an EXTREMELY STRICT quality checker. Review the content critically. "
                "REJECT on first attempt if: missing '24 hours', not emphasizing eco-friendly, too generic, or lacks punch. "
                "ONLY approve if it's truly exceptional and meets ALL criteria. "
                "Return JSON with: approved (bool), feedback (string with specific improvements needed), content (the reviewed text)."
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
    print("\nBuilding workflow with conditional branches and loop...")
    print("  Writer → Quality Checker")
    print("     ↓ (approved)      ↓ (rejected)")
    print("  Publisher        Editor → Writer (loop)")
    print()
    
    workflow = (
        WorkflowBuilder()
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
    
    # Execute workflow
    print("=" * 80)
    print("🔍 User Query: Create a tagline for an eco-friendly water bottle")
    print("=" * 80)
    print("\n⚙️  Executing workflow with conditional branching...\n")
    print("💡 The quality checker will decide: approve → publish OR reject → revise")
    print("=" * 80)
    
    print("\n📝 Writer: Creating initial content...")
    
    request = AgentExecutorRequest(
        messages=[ChatMessage(Role.USER, text="Create a compelling tagline for an eco-friendly water bottle that keeps drinks cold for 24 hours.")],
        should_respond=True
    )
    
    # Track iterations
    iteration_count = 0
    
    # Process events in real-time to show workflow progress
    events = await workflow.run(request)
    
    # Parse events to show what happened
    print("\n" + "=" * 80)
    print("📊 WORKFLOW EXECUTION SUMMARY")
    print("=" * 80)
    
    # Count events by agent
    writer_count = 0
    quality_count = 0
    publisher_count = 0
    
    for event in events:
        if hasattr(event, 'executor_id'):
            if event.executor_id == 'writer':
                writer_count += 1
            elif event.executor_id == 'quality_checker':
                quality_count += 1
            elif event.executor_id == 'publisher':
                publisher_count += 1
    
    # Calculate iterations (writer runs minus 1 for initial)
    iterations = writer_count - 1
    
    print(f"\n📝 Writer executed: {writer_count} time(s)")
    print(f"🔍 Quality Checker executed: {quality_count} time(s)")
    print(f"📤 Publisher executed: {publisher_count} time(s)")
    
    if iterations > 0:
        print(f"\n🔄 Content was rejected {iterations} time(s) and revised!")
    else:
        print(f"\n✅ Content was approved on first attempt!")
    
    outputs = events.get_outputs()
    
    if outputs:
        print("\n" + "=" * 80)
        print("🎉 FINAL OUTPUT")
        print("=" * 80)
        print(outputs[0])
    
    print("\n" + "=" * 80)
    print("✅ Workflow completed!")
    print("=" * 80)
    
    # Summary
    print("\n" + "=" * 80)
    print("🎓 WORKFLOWBUILDER KEY CONCEPTS")
    print("=" * 80)
    print("""
✅ Conditional routing with edge conditions
✅ Multiple execution paths (approved/rejected)
✅ Loops for iterative improvement
✅ Structured outputs with Pydantic for reliable decisions
✅ Complex graph-based workflows

Difference from SequentialBuilder:
- SequentialBuilder: Linear, predictable path (A → B → C)
- WorkflowBuilder: Branching, loops, conditional logic

When to use WorkflowBuilder:
- Approval workflows with accept/reject paths
- Iterative improvement loops
- Complex decision trees
- Multi-path execution based on conditions
    """)
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(main())
