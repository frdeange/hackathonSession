# ============================================================================
# SAMPLE 2: Agent with DevUI - Interactive Web Interface
# ============================================================================
# This example demonstrates how to launch an interactive web interface using
# Microsoft Agent Framework's DevUI for testing agents during development.
#
# DevUI provides:
# - Interactive web chat interface
# - Real-time response streaming
# - OpenAI-compatible REST API endpoints
# - Multiple entity management
# ============================================================================

import os
from agent_framework.azure import AzureOpenAIChatClient
from agent_framework.devui import serve
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Azure OpenAI Chat client
# Note: DevUI's serve() function manages the client lifecycle,
# so we don't need to use 'async with' context manager here.
# The serve() function will handle cleanup when the server stops.
azure_client = AzureOpenAIChatClient(
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    async_credential=DefaultAzureCredential(),
)

# Create an agent
axway_agent = azure_client.create_agent(
    name="Axway Agent",
    instructions="You are a helpful assistant for Axway",
    tools=[],
)

# Launch DevUI web server
# This will:
# - Start a web server (default port 8080)
# - Open your browser automatically
# - Provide an interactive chat interface
# - Keep running until you press Ctrl+C
#
# The serve() function handles the async event loop and client cleanup internally
serve(
    entities=[axway_agent],
    auto_open=True,
    tracing_enabled=True
)
