# 🤖 AI Agents & Azure OpenAI Hackathon

<div align="center">

![Azure](https://img.shields.io/badge/Azure-OpenAI-0078D4?style=for-the-badge&logo=microsoft-azure)
![AI Agents](https://img.shields.io/badge/AI-Agents-purple?style=for-the-badge&logo=robot)
![Hands-On](https://img.shields.io/badge/Learning-Hands--On-green?style=for-the-badge)

**Master the Art of Building Intelligent AI Agents with Azure AI Foundry**

*From your first AI chat to sophisticated multi-agent orchestration*

</div>

---

## 🚀 **What You'll Build Today**

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0;">

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; color: white;">

### 💬 **Interactive AI Chats**
- Modern web interfaces with Chainlit
- Real-time streaming responses
- Personalized conversation experiences

</div>

<div style="background: linear-gradient(135deg, #b141bdff 0%, #f5576c 100%); padding: 20px; border-radius: 10px; color: white;">

### 🤖 **Intelligent AI Agents**
- Specialized domain agents (travel, assistant)
- Memory and context management
- Azure AI Foundry integration

</div>

<div style="background: linear-gradient(135deg, #033560ff 0%, #00f2fe 100%); padding: 20px; border-radius: 10px; color: white;">

### 🛠️ **Powerful Tool Integration**
- Search capabilities with AI Search
- Model Context Protocol (MCP)
- Custom tool development

</div>

<div style="background: linear-gradient(135deg, #05582177 0%, #38f9d7 100%); padding: 20px; border-radius: 10px; color: white;">

### 🎼 **Agent Orchestration**
- Multi-agent coordination
- Semantic Kernel framework
- Enterprise-scale patterns

</div>

</div>

---

## 📚 **Learning Journey**

### 🎯 **EX1: FirstAIChat** → *Build Your Foundation*
**🕒 Duration:** 30 minutes | **📊 Difficulty:** Beginner

<div style="background: #e8f5e9; padding: 15px; border-radius: 8px; border-left: 4px solid #28a745; margin: 10px 0;">

**Create Your First AI Chat Service with Azure OpenAI**

✅ **What You'll Learn:**
- Azure OpenAI SDK fundamentals
- Interactive chat loops and personalization
- Modern web interfaces with Chainlit
- Token usage and optimization

🏆 **Challenges Available:**
- [Interactive Chat Loop](./EX1-FirstAIChat/challenge/ex-ch1-aoaiSDK.md) - Personal AI assistant
- [Chainlit Web Chat](./EX1-FirstAIChat/challenge/ex1-ch2-aoaiChat.md) - Memory-enabled web interface

</div>

### 🤖 **EX2: FirstAgent** → *Enter the Agent World*
**🕒 Duration:** 30 minutes | **📊 Difficulty:** Beginner to Intermediate

<div style="background: #e3f2fd; padding: 15px; border-radius: 8px; border-left: 4px solid #007bff; margin: 10px 0;">

**Create Your First Intelligent Agent with Azure AI Foundry**

✅ **What You'll Learn:**
- AI Agent architecture and benefits
- Azure AI Foundry Agent Service
- Thread-based conversation management
- Agent specialization for domains

🏆 **Challenges Available:**
- [Travel Companion Agent](./EX2-FirstAgent/challenge/ex2-travel-companion-challenge.md) - Specialized travel advisor with memory

</div>

### 🔧 **EX3: AgentWithTools** → *Empower with Tools*
**🕒 Duration:** 60 minutes | **📊 Difficulty:** Intermediate to Advanced

**Enhance Your Agent with Powerful Tools and Integrations**

✅ **What You'll Learn:**
- Function Calling fundamentals
- OpenAPI specification integration
- Model Context Protocol (MCP)
- Multi-agent collaboration patterns
- Azure AI Search integration
- Structured outputs with Pydantic

🏆 **4 Challenges Available:**
- [Function Calling](./EX3-AgentWithTools/challenge/ex3-ch1-FunctionCalling.md) - Tool integration basics
- [OpenAPI Integration](./EX3-AgentWithTools/challenge/ex3-ch2-OpenAPI.md) - REST API connections
- [MCP Integration](./EX3-AgentWithTools/challenge/ex3-ch3-MCP.md) - Context protocol
- [Multi-Agent System](./EX3-AgentWithTools/challenge/ex3-ch4-MultiAgent.md) - Agent collaboration

---

### 🎼 **EX4: AgentOrchestrationService** → *Coordinate Multiple Agents*
**🕒 Duration:** 45 minutes | **📊 Difficulty:** Advanced

**Master Multi-Agent Coordination with Azure AI Foundry Agents**

✅ **What You'll Learn:**
- Multi-agent architecture with Azure AI Foundry
- Agent handoff patterns and orchestration
- Complex workflow coordination
- GitHub integration and OpenAPI specs

🏆 **Challenge Available:**
- [Multi-Agent System](./EX4-AgentOrchestrationService/challenge/ex4-ch1-AgentsOrchestration.md) - Coordinated agent workflows

---

### ⚡ **EX5: AgentOrchestrationAgentFramework** → *Microsoft Agent Framework*
**🕒 Duration:** 60 minutes | **📊 Difficulty:** Intermediate to Advanced

**Build Production-Ready Agents with Microsoft's Open-Source Framework**

✅ **What You'll Learn:**
- Microsoft Agent Framework (Python + .NET)
- Graph-based workflow orchestration
- Sequential and conditional agent patterns
- DevUI for interactive testing
- MCP (Model Context Protocol) integration
- WorkflowBuilder and SequentialBuilder patterns

📚 **6 Progressive Samples:**
1. Simple Agent - Basic agent creation fundamentals
2. Agent DevUI - Interactive web-based testing
3. Agent with Tools - Function calling integration
4. Sequential Builder - Linear agent workflows
5. Workflow Builder - Conditional branching & loops
6. Workflow DevUI - Visual workflow testing

🏆 **3 Challenges Available:**
- [Microsoft Learn MCP Agent](./EX5-AgentOrchestrationAgentFramework/challenge/ex5-ch1-MCPAgent.md) - Documentation assistant (30 min)
- [Customer Service Chatbot](./EX5-AgentOrchestrationAgentFramework/challenge/ex5-ch2-ChatbotPipeline.md) - Sequential pipeline (30 min)
- [Loan Approval System](./EX5-AgentOrchestrationAgentFramework/challenge/ex5-ch3-LoanApproval.md) - Complex branching (40 min)

---

## 🛠️ **Quick Start Guide**

### 📋 **Prerequisites**

<table>
<tr>
<td>

**🔧 Technical Requirements**
- Azure subscription with OpenAI access
- Python 3.8+ installed
- VS Code (recommended)
- Git for version control

</td>
<td>

**🧠 Knowledge Prerequisites**
- Basic Python programming
- REST API concepts
- Cloud services familiarity
- JSON data structures

</td>
</tr>
</table>

### ⚡ **Environment Setup**

```bash
# 1. Clone the repository
git clone <your-repository-url>
cd hackathonSession

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment variables
# Copy and edit your .env file with Azure credentials
cp .env.example .env
# Edit .env with your Azure credentials
```

### 🎯 **Start Learning**

1. **🏁 Begin with EX1** - Build your foundation with basic AI chats
2. **📈 Progress sequentially** - Each exercise builds on the previous
3. **🏆 Complete challenges** - Hands-on practice with guided exercises
4. **🚀 Experiment freely** - Modify examples and try new ideas

---

## 🎯 **Learning Outcomes**

<div align="center">

| **Skill Area** | **What You'll Master** |
|---|---|
| 🤖 **AI Agent Development** | Create, configure, and deploy intelligent agents |
| 💬 **Conversational AI** | Build engaging chat experiences with memory |
| 🔧 **Tool Integration** | Connect agents to external data and services |
| 🎼 **Orchestration** | Coordinate multiple agents for complex workflows |
| 🌐 **Modern Interfaces** | Deploy web-based AI applications |
| ☁️ **Azure AI Services** | Leverage enterprise-grade AI infrastructure |

</div>

---

## 📁 **Repository Structure**

```
📦 AI Agents Hackathon
├── 📝 requirements.txt                        # Python dependencies
├── 🎯 EX1-FirstAIChat/                       # Foundation: Azure OpenAI basics
│   ├── 📘 samples/                            # Working examples and demos
│   ├── 🏆 challenge/                          # Hands-on practice exercises
│   └── 📚 README.md                           # Detailed instructions
├── 🤖 EX2-FirstAgent/                        # Core: AI Agent fundamentals
│   ├── 📘 samples/                            # Agent examples and integrations
│   ├── 🏆 challenge/                          # Agent development challenges
│   └── 📚 README.md                           # Agent-specific guidance
├── 🔧 EX3-AgentWithTools/                    # Enhancement: Tools & MCP
│   ├── 📘 samples/                            # Function calling, OpenAPI, MCP
│   ├── 🏆 challenge/                          # 4 progressive challenges
│   └── 📚 README.md                           # Tool integration guide
├── 🎼 EX4-AgentOrchestrationService/         # Multi-agent: Azure AI Foundry
│   ├── 📘 samples/                            # Orchestration examples
│   ├── 🏆 challenge/                          # Multi-agent coordination
│   └── 📚 README.md                           # Orchestration patterns
└── ⚡ EX5-AgentOrchestrationAgentFramework/  # Framework: Microsoft Agent Framework
    ├── 📘 samples/                            # 6 progressive samples
    ├── 🏆 challenge/                          # 3 comprehensive challenges
    └── 📚 README.md                           # Framework deep dive
```

---

## 🎨 **Featured Examples**

### 💬 **Interactive Chat Experiences**
- **Personal AI Assistant** - Customizable conversation companion
- **Travel Planning Bot** - Specialized domain knowledge agent
- **Memory-Enabled Chat** - Context-aware conversations

### 🤖 **Intelligent Agents**
- **Azure AI Foundry Agents** - Enterprise-grade agent platform
- **Microsoft Agent Framework** - Open-source orchestration framework
- **Specialized Domain Experts** - Travel, finance, support advisors
- **Multi-Agent Systems** - Coordinated workflows and collaboration

### 🔧 **Advanced Integrations**
- **Chainlit Web Interfaces** - Modern, responsive chat UIs
- **DevUI Interactive Testing** - Browser-based agent visualization
- **Azure AI Search** - Knowledge base integration
- **Model Context Protocol (MCP)** - Standardized context management
- **Function Calling & Tools** - External API integrations
- **Graph-Based Workflows** - Conditional branching and loops

---

## 🆘 **Support & Resources**

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin: 20px 0;">

<div style="background: #e3f2fd; padding: 15px; border-radius: 8px; color: #000;">

### 📚 **Documentation**
- Detailed README in each exercise
- Inline code comments
- Architecture explanations

</div>

<div style="background: #e8f5e9; padding: 15px; border-radius: 8px; color: #000;">

### 🏆 **Challenges**
- Step-by-step guided exercises
- Multiple difficulty levels
- Complete solutions provided

</div>

<div style="background: #fff9e6; padding: 15px; border-radius: 8px; color: #000;">

### 🛠️ **Troubleshooting**
- Common issues and solutions
- Environment setup guides
- Debug tips and tricks

</div>

<div style="background: #ffebee; padding: 15px; border-radius: 8px; color: #000;">

### 🌐 **External Resources**
- [Azure AI Foundry Docs](https://docs.microsoft.com/azure/ai-foundry/)
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)
- [Chainlit Documentation](https://docs.chainlit.io/)
- [Model Context Protocol](https://modelcontextprotocol.io/)

</div>

</div>

---

## 🎉 **Ready to Start?**

<div align="center" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; color: white; margin: 20px 0;">

### 🚀 **Your AI Agent Journey Begins Now!**

**Start with [EX1-FirstAIChat](./EX1-FirstAIChat/) to build your foundation, then progress through each exercise to become an AI Agent expert.**

*Transform from AI curious to AI capable in just one day!* ⚡

[**🎯 Start EX1: FirstAIChat →**](./EX1-FirstAIChat/)

</div>

---

<div align="center">

*Built with ❤️ for AI Developers | © 2025*

![Footer](https://img.shields.io/badge/AI-Powered%20Learning-blue?style=flat-square) ![Level](https://img.shields.io/badge/Level-Beginner%20to%20Advanced-green?style=flat-square) ![Hands-On](https://img.shields.io/badge/Format-Hands--On-orange?style=flat-square)

</div>

