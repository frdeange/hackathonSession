# ============================================================================
# SAMPLE 1: Simple Agent with Microsoft Agent Framework
# ============================================================================
# This example is based on:
# https://github.com/microsoft/agent-framework/blob/main/python/samples/getting_started/minimal_sample.py
#
# Shows how to create a basic agent using Microsoft Agent Framework with:
# - Simple configuration with Azure OpenAI
# - Agent definition with basic instructions
# - Single query execution
# 
# Microsoft Agent Framework is a comprehensive multi-language framework for building,
# orchestrating, and deploying AI agents with support for Python and .NET
# ============================================================================

# 0. REQUIRED IMPORTS
# ---------------------------------------------------------------------
# asyncio: Library for asynchronous programming in Python
# os: To access environment variables
# dotenv: To load environment variables from .env file
# agent_framework.azure: Azure OpenAI client from Agent Framework
# azure.identity: Azure authentication using credentials
# ---------------------------------------------------------------------
import asyncio
import os
from dotenv import load_dotenv
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import AzureCliCredential

# Load environment variables from .env file
load_dotenv()

# 1. ENVIRONMENT VARIABLES CONFIGURATION
# ---------------------------------------------------------------------
# Microsoft Agent Framework uses the following variables for Azure OpenAI:
# - AZURE_OPENAI_ENDPOINT: Azure OpenAI endpoint URL
# - AZURE_OPENAI_RESPONSES_DEPLOYMENT_NAME: Model deployment name
# - AZURE_OPENAI_API_VERSION: API version (e.g., 2024-10-01-preview)
# - AZURE_OPENAI_API_KEY: (Optional) API key if not using AzureCliCredential
#
# Note: These variables can be set in .env file or passed directly
# to the client constructor
# ---------------------------------------------------------------------


# 2. WHAT IS MICROSOFT AGENT FRAMEWORK?
# ---------------------------------------------------------------------
# Microsoft Agent Framework is a comprehensive framework that provides:
#
# ✅ High-Level Abstraction:
#    - Simplifies agent creation without dealing with low-level details
#    - Consistent API across different providers (Azure OpenAI, OpenAI, Anthropic, etc.)
#    - Automatic conversation and context management
#
# ✅ Agent Orchestration:
#    - Graph-based workflows to connect multiple agents
#    - Orchestration patterns: sequential, parallel, conditional
#    - Support for human-in-the-loop and checkpointing
#
# ✅ Tool Integration:
#    - Native function calling
#    - Support for OpenAPI specifications
#    - Model Context Protocol (MCP) integration
#
# ✅ Enterprise Features:
#    - Observability with integrated OpenTelemetry
#    - Customizable middleware
#    - DevUI for development and debugging
#
# Differences with Azure AI Foundry Agents:
# - Agent Framework: Open-source framework, multi-provider, local or cloud
# - AI Foundry Agents: Managed service in Azure with agents-as-a-service
# ---------------------------------------------------------------------


# 3. CREATE A SIMPLE AGENT
# ---------------------------------------------------------------------
# AzureOpenAIChatClient is one of the available clients in Agent Framework
# Other available clients:
# - OpenAIChatClient: For using OpenAI directly
# - AzureOpenAIChatClient: For Azure OpenAI with Chat API
# - AzureOpenAIAssistantsClient: For Azure OpenAI Assistants API
#
# The create_agent() method creates an agent with:
# - name: Agent identifier name
# - instructions: System prompt that defines the agent's behavior
#
# The created agent is a reusable object that can execute multiple queries
# ---------------------------------------------------------------------
async def main():
    """
    Main function demonstrating the creation and use of a simple agent.
    
    This example shows the most basic pattern of Microsoft Agent Framework:
    1. Create a chat client
    2. Create an agent with instructions
    3. Execute a query with the run() method
    """
    
    # Create the Azure OpenAI Responses client
    # AzureCliCredential uses 'az login' authentication
    # Alternatively, api_key can be used instead of credential
    agent = AzureOpenAIChatClient(
        # endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],  # Optional, read from env
        deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],  # Optional
        api_version=os.environ["AZURE_OPENAI_API_VERSION"],  # Optional
        # api_key=os.environ["AZURE_OPENAI_API_KEY"],  # Optional if using credential
        credential=AzureCliCredential(),  # Uses az login for authentication
    ).create_agent(
        name="HaikuBot",
        instructions="You are an upbeat assistant that writes beautifully and creatively.",
    )

    # 4. RUN THE AGENT
    # ---------------------------------------------------------------------
    # The run() method is the simplest way to interact with an agent:
    # - Accepts a string with the user query
    # - Returns the agent's response directly as a string
    # - Internally manages all communication with the model
    # 
    # For more complex cases, Agent Framework also offers:
    # - run_stream(): To receive streaming responses
    # - Multi-turn conversation management with threads
    # - Integration with workflows to orchestrate multiple agents
    # ---------------------------------------------------------------------
    print("=" * 80)
    print("🤖 SIMPLE AGENT WITH MICROSOFT AGENT FRAMEWORK")
    print("=" * 80)
    print("\n📝 Query: Write a haiku about Microsoft Agent Framework\n")
    
    result = await agent.run("Write a haiku about Microsoft Agent Framework.")
    
    print("💬 Agent Response:")
    print("-" * 80)
    print(result)
    print("-" * 80)
    
    print("\n✅ Example completed successfully!")
    print("\n💡 Next step: Go to ex5-s2-AgentWithTools.py to learn")
    print("   how to add tools/functions to your agents.")


# 5. ADVANTAGES OF MICROSOFT AGENT FRAMEWORK
# ---------------------------------------------------------------------
# ✅ Simplicity: Just 3 lines of code to create and use an agent
# ✅ Flexibility: Easy to switch between different providers (OpenAI, Azure, etc.)
# ✅ Scalability: Same pattern for simple agents or complex workflows
# ✅ Portability: Python or .NET code with consistent APIs
# ✅ Production-ready: Observability, middleware, and best practices built-in
#
# Quick comparison with other approaches:
# - Direct Azure OpenAI SDK: More control but more boilerplate code
# - LangChain: Similar but Agent Framework is officially from Microsoft
# - Azure AI Foundry Agents: Managed service vs code framework
# ---------------------------------------------------------------------


# 6. ADDITIONAL RESOURCES
# ---------------------------------------------------------------------
# 📚 Official Documentation: https://learn.microsoft.com/agent-framework/
# 🔗 GitHub Repository: https://github.com/microsoft/agent-framework
# 🎓 Tutorials: https://learn.microsoft.com/agent-framework/tutorials/overview
# 💬 Discord: https://discord.gg/b5zjErwbQM
# ---------------------------------------------------------------------


if __name__ == "__main__":
    # Run the main function asynchronously
    asyncio.run(main())
