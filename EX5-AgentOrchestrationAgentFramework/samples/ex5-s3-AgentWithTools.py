# ============================================================================
# SAMPLE 3: Agent with Tools (Function Calling) - Microsoft Agent Framework
# ============================================================================
# This example is based on:
# https://github.com/microsoft/agent-framework/blob/main/python/samples/getting_started/minimal_sample.py
#
# Shows how to create an agent with custom tools/functions using Microsoft Agent Framework:
# - Define Python functions as tools
# - Register tools with an agent
# - Agent automatically calls tools when needed
# - Handle tool responses and multi-step reasoning
# 
# Function calling allows agents to interact with external systems, APIs, databases,
# and perform actions beyond text generation.
# ============================================================================

# 0. REQUIRED IMPORTS
# ---------------------------------------------------------------------
# asyncio: Library for asynchronous programming
# random: For generating random data in example functions
# typing.Annotated: For type hints with metadata (used in tool definitions)
# agent_framework.azure: Azure OpenAI client from Agent Framework
# azure.identity: Azure authentication
# ---------------------------------------------------------------------
import os
import asyncio
from random import randint
from typing import Annotated
from dotenv import load_dotenv
from agent_framework.azure import AzureAIAgentClient
from azure.identity import AzureCliCredential

# Load environment variables
load_dotenv()


# 1. DEFINING TOOLS/FUNCTIONS
# ---------------------------------------------------------------------
# In Microsoft Agent Framework, tools are simply Python functions with:
# - Type hints for all parameters (required)
# - Docstrings describing what the function does (required)
# - Annotated types to provide parameter descriptions (recommended)
#
# The framework automatically:
# - Generates OpenAI function calling schema from the function signature
# - Calls the function when the agent decides to use it
# - Passes the result back to the agent for further reasoning
#
# Key points:
# - Use Annotated[type, "description"] for parameters
# - Write clear docstrings (the agent uses this to decide when to call the function)
# - Return values should be JSON-serializable (strings, dicts, lists, etc.)
# ---------------------------------------------------------------------

def get_weather(
    location: Annotated[str, "The location to get the weather for."],
) -> str:
    """Get the weather for a given location.
    
    This function simulates a weather API call. In a real application,
    you would call an actual weather service API here.
    
    Args:
        location: The city or location name to get weather for
        
    Returns:
        A string describing the current weather conditions
    """
    # Simulate weather data - in production, call a real API
    conditions = ["sunny", "cloudy", "rainy", "stormy"]
    temperature = randint(10, 30)
    condition = conditions[randint(0, 3)]
    
    return f"The weather in {location} is {condition} with a high of {temperature}°C."


def get_time(
    timezone: Annotated[str, "The timezone to get the time for (e.g., 'UTC', 'PST', 'EST')"],
) -> str:
    """Get the current time for a specific timezone.
    
    This function simulates getting time for different timezones.
    In a real application, you would use proper timezone libraries.
    
    Args:
        timezone: The timezone identifier (e.g., 'UTC', 'PST', 'EST')
        
    Returns:
        A string with the current time in the specified timezone
    """
    # Simulate time data - in production, use datetime with timezone support
    hour = randint(0, 23)
    minute = randint(0, 59)
    
    return f"The current time in {timezone} is {hour:02d}:{minute:02d}."


def calculate(
    operation: Annotated[str, "The mathematical operation: 'add', 'subtract', 'multiply', or 'divide'"],
    a: Annotated[float, "The first number"],
    b: Annotated[float, "The second number"],
) -> str:
    """Perform a mathematical calculation.
    
    This function demonstrates how to handle multiple parameters and
    different operation types in a tool.
    
    Args:
        operation: The type of calculation to perform
        a: First operand
        b: Second operand
        
    Returns:
        A string with the calculation result
    """
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else "Error: Division by zero",
    }
    
    if operation.lower() not in operations:
        return f"Error: Unknown operation '{operation}'. Use: add, subtract, multiply, or divide."
    
    result = operations[operation.lower()](a, b)
    return f"The result of {a} {operation} {b} is {result}."


# 2. CREATING AN AGENT WITH TOOLS
# ---------------------------------------------------------------------
# To create an agent with tools in Microsoft Agent Framework:
#
# 1. Define your functions (as shown above)
# 2. Create a chat client (AzureOpenAIChatClient, OpenAIChatClient, etc.)
# 3. Call create_agent() and pass functions via the 'tools' parameter
#
# The 'tools' parameter accepts:
# - A single function: tools=get_weather
# - Multiple functions as a list: tools=[get_weather, get_time, calculate]
# - Function objects or callable classes
#
# The agent will automatically:
# - Analyze the user's request
# - Decide which tool(s) to call (if any)
# - Call the tools with appropriate parameters
# - Use the tool results to formulate the final response
# ---------------------------------------------------------------------

async def main():
    """
    Main function demonstrating an agent with multiple tools.
    
    This example shows how to:
    1. Define multiple tool functions
    2. Register tools with an agent
    3. Let the agent automatically decide when and how to use tools
    """
    
    print("=" * 80)
    print("🛠️  AGENT WITH TOOLS - MICROSOFT AGENT FRAMEWORK")
    print("=" * 80)
    print("\nInitializing agent with tools: get_weather, get_time, calculate")
    print("-" * 80)
    
    # Create Azure AI Agent client with authentication
    # Important: Use 'async with' context manager to ensure proper cleanup
    # This prevents "Unclosed client session" warnings by properly closing HTTP connections
    async with AzureAIAgentClient(
        project_endpoint=os.getenv("AI_FOUNDRY_ENDPOINT"),
        model_deployment_name=os.getenv("AI_FOUNDRY_DEPLOYMENT_NAME"),
        async_credential=AzureCliCredential()
    ) as chat_client:
        
        # Create an agent with multiple tools
        # The agent can now call any of these functions as needed
        agent = chat_client.create_agent(
            name="MultiToolAgent",
            instructions=(
                "You are a helpful assistant with access to weather, time, and calculator tools. "
                "Use these tools to answer user questions accurately. "
                "When you use a tool, explain what you're doing and why."
            ),
            tools=[get_weather, get_time, calculate],  # Register all tools
        )
        
        # 3. TEST THE AGENT WITH DIFFERENT QUERIES
        # ---------------------------------------------------------------------
        # The following queries will trigger different tools:
        # - Weather query → calls get_weather()
        # - Time query → calls get_time()
        # - Math query → calls calculate()
        # - Complex query → may call multiple tools
        # ---------------------------------------------------------------------
        
        test_queries = [
            "What's the weather like in Seattle?",
            "What time is it in Tokyo (JST timezone)?",
            "Can you multiply 15 by 7?",
            "Compare the weather in Paris and London, then tell me what time it is in UTC.",
        ]
        
        for i, query in enumerate(test_queries, 1):
            print(f"\n{'=' * 80}")
            print(f"🔍 Query {i}: {query}")
            print("=" * 80)
            
            # Run the agent - it will automatically call tools as needed
            result = await agent.run(query)
            
            print(f"\n💬 Agent Response:")
            print("-" * 80)
            print(result)
            print("-" * 80)
        
        print("\n" + "=" * 80)
        print("✅ All queries completed successfully!")
        print("\n💡 Next step: Go to ex5-s4-AgentWorkflow.py to learn")
        print("   how to orchestrate multiple agents in workflows.")
        print("=" * 80)
    
    # Note: The 'async with' block ensures the client is properly closed
    # when the function exits, preventing resource leaks and warnings


# 4. HOW TOOL CALLING WORKS
# ---------------------------------------------------------------------
# Behind the scenes, when you run an agent with tools:
#
# 1. Agent receives user query
# 2. Agent analyzes query and available tools
# 3. Agent decides which tool(s) to call (if any)
# 4. Framework calls the selected tools with parameters
# 5. Tool results are sent back to the agent
# 6. Agent uses results to generate final response
# 7. Response is returned to the user
#
# This happens automatically - you just define functions and register them!
# ---------------------------------------------------------------------


# 5. BEST PRACTICES FOR TOOLS
# ---------------------------------------------------------------------
# ✅ Clear Docstrings: Describe what the function does clearly
# ✅ Type Annotations: Always use type hints for parameters
# ✅ Annotated Parameters: Use Annotated to provide parameter descriptions
# ✅ Error Handling: Return error messages as strings, don't raise exceptions
# ✅ JSON Serializable: Return strings, dicts, lists (not complex objects)
# ✅ Focused Functions: Each function should do one thing well
# ✅ Deterministic: Same inputs should produce same outputs when possible
# ✅ Resource Management: Use 'async with' for clients to ensure proper cleanup
#
# Common Tool Use Cases:
# - API calls (weather, news, stock prices, etc.)
# - Database queries
# - File operations (read, write, search)
# - Calculations and data processing
# - External service integration (email, calendar, etc.)
#
# Important: Resource Management
# Always use context managers (async with) when creating clients that maintain
# HTTP connections. This ensures connections are properly closed and prevents
# "Unclosed client session" warnings.
#
# Example:
#   async with AzureAIAgentClient(...) as client:  # ✅ Correct
#       agent = client.create_agent(...)
#   
#   client = AzureAIAgentClient(...)  # ❌ May cause resource leaks
# ---------------------------------------------------------------------


# 6. ADDITIONAL RESOURCES
# ---------------------------------------------------------------------
# 📚 Tool Documentation: https://learn.microsoft.com/agent-framework/user-guide/agents/tools
# 🔗 Function Calling Guide: https://github.com/microsoft/agent-framework/tree/main/python/samples/getting_started/agents
# 📖 OpenAPI Integration: Agent Framework also supports OpenAPI specifications
# 🔧 MCP Protocol: Model Context Protocol for standardized tool definitions
# ---------------------------------------------------------------------


if __name__ == "__main__":
    # Run the main function asynchronously
    asyncio.run(main())
