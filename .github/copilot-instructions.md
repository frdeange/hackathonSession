# AI Agent Hackathon - Copilot Instructions

## Language Conventions
- Use English for all code comments, docstrings, and messages.

## Project Architecture

This is a **progressive learning hackathon** with 5 exercises (EX1-EX5) teaching Azure AI agent development from basic chat to enterprise orchestration. Each exercise contains `samples/` (working examples) and `challenge/` (hands-on exercises with solutions).


### Exercise Progression
1. **EX1-FirstAIChat**: Azure OpenAI SDK basics, Chainlit web UI
2. **EX2-FirstAgent**: Azure AI Foundry agents, thread-based conversations
3. **EX3-AgentWithTools**: Function calling, OpenAPI integration, MCP protocol, multi-agent systems
4. **EX4-AgentOrchestrationService**: Azure AI Foundry multi-agent orchestration
5. **EX5-AgentOrchestrationAgentFramework**: Microsoft Agent Framework (WorkflowBuilder, SequentialBuilder, DevUI)

## File Naming Conventions

**Critical Pattern**: All files follow strict naming: `ex{N}-{type}{N}-{name}.{ext}`

- **Samples**: `ex1-s1-aoai.py`, `ex2-s2-agentChainlit-aad.py`
- **Challenges**: `ex1-ch1-aoaiSDK.md`, `ex5-ch3-LoanApproval.md`
- **Solutions**: `ex1-ch1-solution.py` (inside `challenge/Solutions/`)

**Authentication Suffix Pattern** (EX2-EX5):
- `-aad.py`: DefaultAzureCredential (development, uses `az login`)
- `-sp.py`: ClientSecretCredential (production, uses service principal)

## Authentication Architecture

### Two Authentication Strategies Throughout

**Development (AAD - Azure Default Credential)**:
```python
from azure.identity import DefaultAzureCredential
credential = DefaultAzureCredential(exclude_environment_credential=True)
```
- Requires: `az login` before running
- Used in: `*-aad.py` files
- Best for: Local development, VS Code integration

**Production (SP - Service Principal)**:
```python
from azure.identity import ClientSecretCredential
credential = ClientSecretCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    client_id=os.getenv("AZURE_CLIENT_ID"),
    client_secret=os.getenv("AZURE_CLIENT_SECRET")
)
```
- Requires: Three environment variables
- Used in: `*-sp.py` files
- Best for: CI/CD, production, non-interactive scenarios

## Environment Variables by Exercise

**EX1** (Azure OpenAI basics):
```
AZURE_OPENAI_ENDPOINT
AZURE_OPENAI_API_KEY
AZURE_OPENAI_DEPLOYMENT_NAME
AZURE_OPENAI_API_VERSION
```

**EX2-EX4** (Azure AI Foundry):
```
AI_FOUNDRY_ENDPOINT
AI_FOUNDRY_DEPLOYMENT_NAME
# Plus authentication vars (AAD or SP)
```

**EX5** (Microsoft Agent Framework):
```
AZURE_OPENAI_ENDPOINT
AZURE_OPENAI_DEPLOYMENT_NAME
AZURE_OPENAI_API_VERSION
# Uses AzureCliCredential by default
```

## Critical Development Workflows

### Running Chainlit Applications
```bash
chainlit run samples/ex1-s2-chainlit.py
# Opens browser at http://localhost:8000
# Uses @cl.on_chat_start, @cl.on_message, @cl.on_chat_end decorators
```

### Running Microsoft Agent Framework DevUI
```python
from agent_framework.devui import serve
serve(entities=[agent], port=8090, auto_open=True)
# Opens browser at http://localhost:8090
# serve() manages client lifecycle automatically
```

### Azure AI Foundry Agent Execution Pattern
```python
# 1. Create agent
agent = project.agents.create_agent(model=deployment, instructions="...")
# 2. Create thread (conversation)
thread = project.agents.threads.create_thread()
# 3. Add message
message = project.agents.messages.create(thread_id=thread.id, role="user", content="...")
# 4. Run agent (blocking)
run = project.agents.runs.create_and_process(thread_id=thread.id, agent_id=agent.id)
# 5. Retrieve response
messages = project.agents.messages.list(thread_id=thread.id, order=ListSortOrder.DESCENDING)
```

### Microsoft Agent Framework Async Patterns

**AzureOpenAIChatClient** - Does NOT support async with:
```python
client = AzureOpenAIChatClient(endpoint=..., credential=AzureCliCredential())
agent = client.create_agent(instructions="...", name="...")
response = await agent.run(messages=[...])
```

**AzureAIAgentClient** - REQUIRES async with:
```python
async with AzureAIAgentClient(endpoint=..., credential=...) as client:
    agent = client.create_agent(instructions="...", tools=[...])
    # Prevents "Unclosed client session" warnings
```

## Microsoft Agent Framework Orchestration Patterns

### SequentialBuilder (High-Level, Linear)
- **Use case**: Simple A → B → C workflows without branching
- **Key feature**: Automatic conversation history management
- **Pattern**:
```python
workflow = SequentialBuilder().participants([writer, reviewer, finalizer]).build()
async for event in workflow.run_stream("prompt"):
    # Process events
```

### WorkflowBuilder (Low-Level, Graphs)
- **Use case**: Conditional branching, loops, complex decision trees
- **Key features**: Conditional edges, custom executors, multiple paths
- **Pattern**:
```python
workflow = (
    WorkflowBuilder()
    .set_start_executor(agent1)
    .add_edge(agent1, agent2, condition=approval_condition)
    .add_edge(agent2, agent3, condition=rejection_condition)
    .build()
)
events = await workflow.run(request)
```

**Conditional Functions**:
```python
def approved_condition(message: Any) -> bool:
    if not isinstance(message, AgentExecutorResponse):
        return True
    assessment = MyModel.model_validate_json(message.agent_run_response.text)
    return assessment.decision == "approve"
```

**Custom Executors** (transforms between agents):
```python
@executor(id="transform")
async def transform_data(response: AgentExecutorResponse, ctx: WorkflowContext[AgentExecutorRequest]) -> None:
    ctx.output.messages = [ChatMessage(Role.USER, text=transformed_text)]
```

## Challenge Structure Pattern

All challenges follow this markdown structure:
1. **Badges**: Difficulty, Time, Challenge number
2. **Objective**: What they'll build
3. **Technical Requirements**: Basic level (mandatory) + Advanced level (bonus)
4. **Getting Started Hints**: Collapsible code snippets
5. **Success Criteria**: Checkboxes for validation
6. **Expected Output**: Example terminal output

**Starter Code**: Challenges include Pydantic models, helper functions, test data when users wouldn't know how to create them (e.g., knowledge bases in EX5-CH2).

## Package Dependencies

Key versions from `requirements.txt`:
- `azure-ai-agents==1.2.0b5` (Azure AI Foundry)
- `azure-ai-projects==1.1.0b3` (Project client)
- `chainlit==2.7.2` (Web UI framework)
- `openai==1.107.1` (OpenAI SDK)
- `semantic-kernel==1.36.2` (Not yet implemented)
- `agent-framework==1.0.0b251028` (Microsoft Agent Framework)

## Common Patterns to Follow

### Error Handling in Agents
- Azure AI Foundry: Check `run.status` for "completed", "failed", "requires_action"
- Tools should return error strings, not raise exceptions
- Always validate Pydantic models with try/except when parsing JSON

### Streaming Responses
- Chainlit: Use `cl.Message(content="").send()` then `msg.stream_token()`
- Agent Framework: Use `run_stream()` and process `WorkflowOutputEvent`

### Resource Cleanup
- Use `with` context managers for Azure AI Foundry clients
- Use `async with` for AzureAIAgentClient only (not AzureOpenAIChatClient)
- Chainlit sessions auto-cleanup via user_session

### Structured Outputs
- Always use `response_format=PydanticModel` for reliable agent-to-agent communication
- WorkflowBuilder relies on structured outputs for conditional routing
- Define clear Pydantic models with descriptive docstrings

## Testing New Code

1. **Environment setup**: Ensure `.env` file exists with required variables
2. **Azure auth**: Run `az login` before testing AAD files
3. **Dependencies**: `pip install -r requirements.txt`
4. **Chainlit apps**: Use `chainlit run <file>` not `python <file>`
5. **Agent Framework**: All entry points use `asyncio.run(main())`

## What NOT to Do

- ❌ Don't mix AAD and SP authentication in same file
- ❌ Don't use `async with` on AzureOpenAIChatClient
- ❌ Don't forget `@executor` decorator for workflow transformations
- ❌ Don't create challenges without starter code for complex data structures
- ❌ Don't use generic SDK versions in code comments - refer to official GitHub samples
- ❌ Don't run Python files directly when they're Chainlit apps

## Key Documentation Sources

All samples reference original GitHub sources in header comments:
- Agent Framework: `https://github.com/microsoft/agent-framework/tree/main/python/samples/getting_started/`
- Specific samples documented in `EX5-AgentOrchestrationAgentFramework/SOURCE_ATTRIBUTION.md`

When creating new samples, always cite the original Microsoft repository location in file headers.
