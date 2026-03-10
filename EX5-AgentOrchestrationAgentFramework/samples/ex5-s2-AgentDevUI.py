# ============================================================================
# SAMPLE 2: Agent with DevUI - Interactive Web Interface
# ============================================================================
# ============================================================================

import os
from agent_framework.azure import AzureOpenAIChatClient
from agent_framework.devui import serve
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Azure OpenAI Chat client
azure_client = AzureOpenAIChatClient(
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    async_credential=DefaultAzureCredential(),
)

# Create an agent
axway_agent = azure_client.create_agent(
    name="Axway Agent DevUI",
    instructions="You are a helpful assistant for Axway",
    tools=[],
)

# Launch DevUI web server
serve(
    entities=[axway_agent],
    auto_open=True,
    tracing_enabled=True
)
