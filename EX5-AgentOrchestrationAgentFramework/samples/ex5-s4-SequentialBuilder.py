# ============================================================================
# SAMPLE 4: SequentialBuilder - High-Level Sequential Workflows
# ============================================================================
# Based on: sequential_agents.py
# https://github.com/microsoft/agent-framework/blob/main/python/samples/getting_started/workflows/orchestration/sequential_agents.py
#
# SequentialBuilder provides a high-level API for creating sequential
# agent chains with automatic conversation management.
# ============================================================================
import os
import asyncio
from dotenv import load_dotenv
from agent_framework import SequentialBuilder, WorkflowOutputEvent, ChatMessage, Role
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import AzureCliCredential
from typing import cast

load_dotenv()


async def main():
    """
    Demonstrates SequentialBuilder for creating sequential agent workflows.
    
    Flow: User Request → Writer → Reviewer → Finalizer → Final Output
    
    Each agent receives the full conversation history and adds to it.
    The output of one agent becomes the input context for the next.
    
    SequentialBuilder is ideal for:
    - Simple sequential agent chains
    - Automatic conversation history management
    - Streaming workflow events
    - Less boilerplate code
    """
    print("\n")
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 23 + "SEQUENTIALBUILDER EXAMPLE" + " " * 30 + "║")
    print("║" + " " * 20 + "High-Level Sequential Workflows" + " " * 27 + "║")
    print("╚" + "═" * 78 + "╝")
    print("\n")
    
    # Create chat client (NOTE: AzureOpenAIChatClient does NOT support async with)
    chat_client = AzureOpenAIChatClient(
        endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        credential=AzureCliCredential()
    )
    
    print("Creating specialized agents...")
    print("-" * 80)
    
    # Create Writer Agent
    writer = chat_client.create_agent(
        instructions=(
            "You are a concise copywriter. "
            "Provide a single, punchy marketing sentence based on the prompt."
        ),
        name="writer",
    )
    
    # Create Reviewer Agent
    reviewer = chat_client.create_agent(
        instructions=(
            "You are a thoughtful reviewer. "
            "Give brief feedback on the previous assistant message."
        ),
        name="reviewer",
    )
    
    # Create Finalizer Agent
    finalizer = chat_client.create_agent(
        instructions=(
            "You are a copywriter finalizer. "
            "Based on the feedback from the reviewer, create the final improved version. "
            "Provide ONLY the final tagline, nothing else."
        ),
        name="finalizer",
    )
    
    # Build sequential workflow
    # SequentialBuilder automatically:
    # - Manages conversation history
    # - Passes messages between agents
    # - Handles input/output formatting
    print("\nBuilding sequential workflow: Writer → Reviewer → Finalizer")
    workflow = SequentialBuilder().participants([writer, reviewer, finalizer]).build()
    
    # Execute workflow with streaming
    print("\n" + "=" * 80)
    print("🔍 User Query: Write a tagline for a budget-friendly eBike")
    print("=" * 80)
    print("\n⚙️  Executing workflow with streaming...\n")
    
    outputs: list[list[ChatMessage]] = []
    
    # Stream events to see real-time progress
    async for event in workflow.run_stream("Write a tagline for a budget-friendly eBike."):
        if isinstance(event, WorkflowOutputEvent):
            outputs.append(cast(list[ChatMessage], event.data))
    
    # Display the final conversation
    if outputs:
        print("📝 Final Conversation History:")
        print("=" * 80)
        for i, msg in enumerate(outputs[-1], start=1):
            name = msg.author_name or ("assistant" if msg.role == Role.ASSISTANT else "user")
            print(f"\n{i:02d}. [{name}]")
            print("-" * 80)
            print(msg.text)
    
    print("\n" + "=" * 80)
    print("✅ Workflow completed!")
    print("=" * 80)
    
    # Summary
    print("\n" + "=" * 80)
    print("🎓 SEQUENTIALBUILDER KEY CONCEPTS")
    print("=" * 80)
    print("""
✅ High-level sequential API
✅ Automatic conversation history management
✅ Streaming support with run_stream()
✅ Less boilerplate code
✅ Each agent builds on previous work

When to use SequentialBuilder:
- Simple sequential agent chains
- Linear workflows without branching
- When you need automatic conversation management
- Quick prototyping of multi-agent systems
    """)
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(main())
