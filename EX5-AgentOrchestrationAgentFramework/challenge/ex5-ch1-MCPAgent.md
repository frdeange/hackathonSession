# 🤖 Challenge 1: Microsoft Learn Documentation Agent with DevUI

<div align="center">

![Challenge 1](https://img.shields.io/badge/Challenge-1-blue?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![Time](https://img.shields.io/badge/Time-30%20minutes-orange?style=for-the-badge)

**Build an AI agent that answers Microsoft technology questions using MCP + DevUI!**

</div>

---

## 🎯 **Objective**

Create an intelligent agent that connects to the **Microsoft Learn Model Context Protocol (MCP)** server to answer questions about Microsoft technologies. Then, deploy it with **DevUI** for an interactive web-based testing experience!

## ✨ **What You'll Learn**

<table>
<tr>
<td>

### 🔄 **Core Skills**
- Integrating MCP servers with agents
- Using Microsoft Learn as a knowledge source
- Building agents with external tools
- Deploying agents with DevUI

</td>
<td>

### 🧠 **AI Concepts**  
- Model Context Protocol (MCP) integration
- Tool/function calling with external services
- Interactive agent testing with web UI
- Production-ready agent deployment

</td>
</tr>
</table>

---

## 📝 **Challenge Description**

Based on **Sample 3** (`ex5-s3-AgentWithTools.py`) and **Sample 2** (`ex5-s2-AgentDevUI.py`), create an agent that:

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; margin: 15px 0; color: white;">

### 🎯 **Your Mission**

1. **📚 Connect to Microsoft Learn MCP** to access Microsoft documentation
2. **🤖 Create an agent** that can answer questions about Azure, .NET, AI, etc.
3. **🌐 Deploy with DevUI** for interactive web-based testing
4. **✅ Test with real queries** about Microsoft technologies

**🌟 Goal**: Build a production-ready documentation assistant accessible via web browser!

</div>

---

## 📋 **Technical Requirements**

### 🥇 **Basic Level (20-25 minutes)** ✅ MAIN GOAL

<div style="background: #d4edda; padding: 15px; border-radius: 8px; border-left: 4px solid #28a745; margin: 10px 0;">

**Create a functional Microsoft Learn agent!**

- [ ] ✅ **MCP Integration**: Connect to Microsoft Learn MCP server
- [ ] ✅ **Agent Creation**: Build agent with clear instructions about its role
- [ ] ✅ **Tool Registration**: Register MCP tools with the agent
- [ ] ✅ **Console Testing**: Test with at least 3 different Microsoft tech queries
- [ ] ✅ **Verify Responses**: Ensure agent provides accurate documentation-based answers

</div>

### 🌟 **Advanced Level (Extra 5-10 minutes)** ⭐ BONUS

<div style="background: #fff3cd; padding: 15px; border-radius: 8px; border-left: 4px solid #ffc107; margin: 10px 0;">

**Deploy with DevUI for professional presentation!**

- [ ] 🔥 **DevUI Integration**: Deploy agent with DevUI web interface
- [ ] 🔥 **Multiple Test Cases**: Test various Microsoft technologies (Azure, AI, .NET, etc.)
- [ ] 🔥 **Error Handling**: Handle cases when documentation isn't found
- [ ] 🔥 **Professional Instructions**: Write clear, helpful agent instructions

</div>

---

## 💡 **Getting Started Hints**

### 🟢 **Basic Level Implementation**

<details>
<summary><b>💡 Hint 1: MCP Server Setup</b></summary>

Connect to the Microsoft Learn MCP server:

```python
from agent_framework.mcp import MCPClient

# Connect to Microsoft Learn MCP server
# URL: https://learn.microsoft.com/api/mcp
mcp_client = MCPClient("https://learn.microsoft.com/api/mcp")

# Get available tools from the MCP server
tools = await mcp_client.get_tools()

# Register tools with your agent
agent = chat_client.create_agent(
    instructions=instructions,
    tools=tools,
    name="Microsoft Learn Assistant"
)
```

</details>

<details>
<summary><b>💡 Hint 2: Agent Instructions</b></summary>

Write clear instructions for your agent:

```python
instructions = (
    "You are a Microsoft Learn documentation assistant. "
    "Use the Microsoft Learn MCP tools to search for accurate, "
    "up-to-date information about Microsoft technologies. "
    "Provide clear, concise answers with relevant links when available."
)
```

</details>

<details>
<summary><b>💡 Hint 3: Testing Queries</b></summary>

Test with diverse queries:
- "What is Azure Functions?"
- "How do I deploy a .NET application to Azure?"
- "Explain Azure OpenAI Service"
- "What are the best practices for Azure AI?"

</details>

### 🔥 **Advanced Level Implementation**

<details>
<summary><b>💡 Hint 4: DevUI Integration</b></summary>

Deploy with DevUI (similar to Sample 2):

```python
from agent_framework.devui import serve
from agent_framework.mcp import MCPClient
from azure_ai.inference.aio import AzureOpenAIChatClient
from azure.identity.aio import AzureCliCredential

async def main():
    # Setup Azure OpenAI client
    credential = AzureCliCredential()
    chat_client = AzureOpenAIChatClient(
        endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        credential=credential
    )
    
    # Connect to Microsoft Learn MCP
    mcp_client = MCPClient("https://learn.microsoft.com/api/mcp")
    tools = await mcp_client.get_tools()
    
    # Create agent with MCP tools
    agent = chat_client.create_agent(
        instructions=instructions,
        tools=tools,
        name="Microsoft Learn Assistant"
    )
    
    # Serve with DevUI
    serve(entities=[agent], port=8090, auto_open=True)
```

</details>

<details>
<summary><b>💡 Hint 5: Error Handling</b></summary>

Handle cases gracefully:

```python
instructions = (
    "You are a Microsoft Learn documentation assistant. "
    "If you cannot find information, politely suggest the user "
    "check the official Microsoft Learn website or rephrase their question."
)
```

</details>

---

## 🎓 **Learning Resources**

### 📚 **Reference Samples**
- **Sample 3**: `ex5-s3-AgentWithTools.py` - Agent with tools/functions
- **Sample 2**: `ex5-s2-AgentDevUI.py` - DevUI deployment example

### 🔗 **Documentation Links**
- [Microsoft Agent Framework - MCP Integration](https://github.com/microsoft/agent-framework)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- [Microsoft Learn](https://learn.microsoft.com/)

---

## ✅ **Success Criteria**

### Basic Level
- ✅ Agent connects to Microsoft Learn MCP server
- ✅ Agent answers questions about Microsoft technologies
- ✅ Responses are accurate and documentation-based
- ✅ Console testing with 3+ different queries works

### Advanced Level  
- ✅ DevUI web interface is accessible at http://localhost:8090
- ✅ Agent can be tested interactively in browser
- ✅ Error handling works gracefully
- ✅ Professional presentation with clear instructions

---

## 🚀 **Expected Output**

### Console Testing (Basic)
```
User: What is Azure Functions?
Agent: Azure Functions is a serverless compute service that lets you run 
event-triggered code without having to explicitly provision or manage 
infrastructure. [Based on Microsoft Learn documentation]

User: How do I use Azure OpenAI?
Agent: Azure OpenAI Service provides REST API access to OpenAI's powerful 
language models. You can deploy models like GPT-4, GPT-3.5-Turbo...
```

### DevUI Testing (Advanced)
- Browser opens automatically to http://localhost:8090
- Dropdown shows "Microsoft Learn Assistant"
- Chat interface allows interactive queries
- Responses include documentation references

---

## 💪 **Challenge Tips**

1. **Start Simple**: Get console version working first before adding DevUI
2. **Test Thoroughly**: Try various Microsoft technologies to verify MCP integration
3. **Read Sample 3**: Understand how tools/functions are registered
4. **Read Sample 2**: Understand DevUI deployment pattern
5. **Clear Instructions**: Write helpful agent instructions for best results

---

## 🎉 **Bonus Ideas**

- Add conversation history to maintain context
- Include source links in responses
- Support follow-up questions
- Add multiple agents (Azure expert, .NET expert, AI expert)

---

<div align="center">

**🌟 Ready to build your Microsoft Learn assistant? Let's go! 🌟**

</div>
