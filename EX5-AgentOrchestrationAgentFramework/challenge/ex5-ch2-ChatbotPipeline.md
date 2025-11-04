# 💬 Challenge 2: Customer Service Chatbot Pipeline

<div align="center">

![Challenge 2](https://img.shields.io/badge/Challenge-2-blue?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![Time](https://img.shields.io/badge/Time-30%20minutes-orange?style=for-the-badge)

**Build a sequential workflow for an intelligent customer service chatbot!**

</div>

---

## 🎯 **Objective**

Create a **sequential workflow** with multiple specialized agents that work together to process customer queries, search a knowledge base, generate responses, and ensure quality - just like a real customer service system!

## ✨ **What You'll Learn**

<table>
<tr>
<td>

### 🔄 **Core Skills**
- Building sequential agent workflows
- Creating specialized agents with distinct roles
- Simulating knowledge base retrieval
- Quality assurance in AI responses

</td>
<td>

### 🧠 **AI Concepts**  
- Sequential workflow orchestration
- Intent classification
- Knowledge retrieval patterns
- Multi-agent collaboration

</td>
</tr>
</table>

---

## 📝 **Challenge Description**

Based on **Sample 4** (`ex5-s4-SequentialBuilder.py`), create a customer service chatbot pipeline with 4 specialized agents:

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; margin: 15px 0; color: white;">

### 🎯 **Your Mission**

**Create a 4-agent sequential pipeline:**

1. **🎯 Intent Classifier** - Classifies query type (FAQ, Order Status, Complaint, Product Info)
2. **📚 Knowledge Retriever** - Searches simulated knowledge base for relevant info
3. **✍️ Response Generator** - Creates natural, friendly customer response
4. **✅ Quality Checker** - Validates response completeness and helpfulness

**🌟 Goal**: Build a complete customer service automation pipeline!

</div>

---

## 🛠️ **Knowledge Base - Starter Code**

<div style="background: #e7f3ff; padding: 15px; border-radius: 8px; border-left: 4px solid #0066cc; margin: 10px 0;">

**📦 Use this simulated knowledge base in your solution:**

```python
# Simulated Knowledge Base for Customer Service
KNOWLEDGE_BASE = {
    "return_policy": {
        "intent": "faq",
        "content": "Our return policy allows returns within 30 days of purchase. Items must be unused and in original packaging. Refunds are processed within 5-7 business days."
    },
    "shipping": {
        "intent": "faq",
        "content": "We offer free standard shipping on orders over $50. Standard shipping takes 5-7 business days. Express shipping (2-3 days) is available for $9.99."
    },
    "warranty": {
        "intent": "faq",
        "content": "All products come with a 1-year manufacturer's warranty covering defects in materials and workmanship. Extended warranties are available at checkout."
    },
    "track_order": {
        "intent": "order_status",
        "content": "To track your order, visit our website and enter your order number in the tracking section. You'll receive email updates at each shipping milestone."
    },
    "cancel_order": {
        "intent": "order_status",
        "content": "Orders can be cancelled within 24 hours of placement. After 24 hours, orders are processed and cannot be cancelled. Please contact support for assistance."
    },
    "product_specs": {
        "intent": "product_info",
        "content": "Detailed product specifications are available on each product page. For technical questions, our support team is available 24/7 via chat or email."
    },
    "complaint_process": {
        "intent": "complaint",
        "content": "We take all complaints seriously. Please provide your order number and detailed description. Our team will respond within 24 hours with a resolution plan."
    }
}

# Helper function to search knowledge base
def search_knowledge_base(intent: str, query: str) -> str:
    """
    Search the knowledge base for relevant information.
    
    Args:
        intent: The classified intent (faq, order_status, complaint, product_info)
        query: The original user query
    
    Returns:
        Relevant knowledge base content or a default message
    """
    # Simple keyword matching for demo purposes
    query_lower = query.lower()
    
    # Search for matching topics
    for topic, data in KNOWLEDGE_BASE.items():
        if data["intent"] == intent:
            # Check if query contains topic keywords
            if any(keyword in query_lower for keyword in topic.split('_')):
                return f"[Knowledge Base - {topic}]: {data['content']}"
    
    # Return generic response for the intent if no specific match
    generic_responses = {
        "faq": "[Knowledge Base]: For general questions, please visit our FAQ page at www.example.com/faq",
        "order_status": "[Knowledge Base]: For order-related queries, please provide your order number for specific assistance.",
        "complaint": "[Knowledge Base]: We apologize for any inconvenience. Please provide details so we can assist you better.",
        "product_info": "[Knowledge Base]: For product information, please visit the product page or contact our support team."
    }
    
    return generic_responses.get(intent, "[Knowledge Base]: No relevant information found.")
```

**💡 Tip**: Copy this code into your solution file and use `search_knowledge_base()` in your Knowledge Retriever agent!

</div>

---

## 📋 **Technical Requirements**

### 🥇 **Basic Level (25-30 minutes)** ✅ MAIN GOAL

<div style="background: #d4edda; padding: 15px; border-radius: 8px; border-left: 4px solid #28a745; margin: 10px 0;">

**Build the complete 4-agent pipeline!**

- [ ] ✅ **Intent Classifier Agent**: Classifies queries into 4 categories
  - FAQ (general questions)
  - Order Status (tracking, cancellation)
  - Complaint (issues, problems)
  - Product Info (specifications, details)

- [ ] ✅ **Knowledge Retriever Agent**: Uses `search_knowledge_base()` function
  - Receives intent from classifier
  - Searches knowledge base
  - Returns relevant information

- [ ] ✅ **Response Generator Agent**: Creates customer-friendly responses
  - Uses knowledge base results
  - Natural, empathetic tone
  - Clear and concise

- [ ] ✅ **Quality Checker Agent**: Validates final response
  - Checks completeness
  - Ensures helpfulness
  - Confirms professional tone

- [ ] ✅ **Sequential Workflow**: Use `SequentialBuilder` to connect agents
- [ ] ✅ **Test Queries**: Test with at least 4 different query types

</div>

### 🌟 **Advanced Level (Extra 10 minutes)** ⭐ BONUS

<div style="background: #fff3cd; padding: 15px; border-radius: 8px; border-left: 4px solid #ffc107; margin: 10px 0;">

**Enhance with structured outputs and streaming!**

- [ ] 🔥 **Structured Outputs**: Use Pydantic models for agent responses
- [ ] 🔥 **Streaming**: Display workflow progress in real-time
- [ ] 🔥 **Enhanced KB**: Expand knowledge base with more topics
- [ ] 🔥 **Fallback Handling**: Handle queries with no KB match gracefully

</div>

---

## 💡 **Getting Started Hints**

### 🟢 **Basic Level Implementation**

<details>
<summary><b>💡 Hint 1: Intent Classifier Agent Instructions</b></summary>

```python
intent_classifier = chat_client.create_agent(
    instructions=(
        "You are an intent classifier for customer service. "
        "Analyze the customer query and classify it into ONE of these categories: "
        "1. FAQ - General questions about policies, shipping, returns "
        "2. ORDER_STATUS - Questions about orders, tracking, cancellation "
        "3. COMPLAINT - Problems, issues, dissatisfaction "
        "4. PRODUCT_INFO - Questions about product specifications "
        "Return ONLY the intent category name in uppercase."
    ),
    name="intent_classifier"
)
```

</details>

<details>
<summary><b>💡 Hint 2: Knowledge Retriever Pattern</b></summary>

The Knowledge Retriever needs to:
1. Receive the intent from the classifier
2. Call `search_knowledge_base(intent, original_query)`
3. Return the knowledge base results

```python
knowledge_retriever = chat_client.create_agent(
    instructions=(
        "You are a knowledge base retriever. "
        "Based on the intent classification, search the knowledge base "
        "and provide relevant information. Include the knowledge base content "
        "in your response."
    ),
    name="knowledge_retriever"
)
```

**Note**: You may need to extract the intent from the previous agent's response.

</details>

<details>
<summary><b>💡 Hint 3: Sequential Workflow</b></summary>

Connect all 4 agents sequentially:

```python
workflow = SequentialBuilder().participants([
    intent_classifier,
    knowledge_retriever,
    response_generator,
    quality_checker
]).build()
```

</details>

<details>
<summary><b>💡 Hint 4: Test Queries</b></summary>

Test with these diverse queries:
- "What's your return policy?" (FAQ)
- "How can I track my order?" (Order Status)
- "I'm unhappy with my purchase" (Complaint)
- "What are the specifications of product X?" (Product Info)

</details>

### 🔥 **Advanced Level Implementation**

<details>
<summary><b>💡 Hint 5: Structured Outputs with Pydantic</b></summary>

Define output models for cleaner agent communication:

```python
from pydantic import BaseModel

class IntentClassification(BaseModel):
    intent: str  # faq, order_status, complaint, product_info
    confidence: float
    query: str

class KnowledgeResult(BaseModel):
    intent: str
    kb_content: str
    query: str

class CustomerResponse(BaseModel):
    response: str
    tone: str  # friendly, empathetic, professional
```

Use with `response_format=IntentClassification` in agent creation.

</details>

<details>
<summary><b>💡 Hint 6: Streaming with run_stream()</b></summary>

See real-time progress:

```python
async for event in workflow.run_stream(user_query):
    if isinstance(event, WorkflowOutputEvent):
        # Process events
        pass
```

</details>

---

## 🎓 **Learning Resources**

### 📚 **Reference Samples**
- **Sample 4**: `ex5-s4-SequentialBuilder.py` - Sequential workflow with 3 agents
- **Sample 1**: `ex5-s1-SimpleAgent.py` - Basic agent creation

### 🔗 **Key Concepts**
- **SequentialBuilder**: Automatic conversation history management
- **Agent Instructions**: Clear, specific role definitions
- **Conversation Context**: Each agent builds on previous work

---

## ✅ **Success Criteria**

### Basic Level
- ✅ 4 agents created with distinct, clear roles
- ✅ Sequential workflow connects agents properly
- ✅ Intent classification works for all 4 categories
- ✅ Knowledge base integration functions correctly
- ✅ Final responses are natural and helpful
- ✅ Successfully tested with 4+ different query types

### Advanced Level  
- ✅ Pydantic models used for structured agent communication
- ✅ Workflow streaming shows real-time progress
- ✅ Expanded knowledge base with additional topics
- ✅ Graceful fallback when KB has no match

---

## 🚀 **Expected Output**

### Example Execution
```
User Query: "What's your return policy?"

📊 FINAL CONVERSATION HISTORY:
================================================================================

01. [user]
What's your return policy?

02. [intent_classifier]
FAQ

03. [knowledge_retriever]
[Knowledge Base - return_policy]: Our return policy allows returns within 30 
days of purchase. Items must be unused and in original packaging. Refunds are 
processed within 5-7 business days.

04. [response_generator]
Thank you for your question! Our return policy is designed to be customer-friendly. 
You can return items within 30 days of purchase as long as they're unused and in 
their original packaging. Once we receive your return, we'll process your refund 
within 5-7 business days. Is there anything else I can help you with?

05. [quality_checker]
✅ Response Quality: APPROVED
The response is complete, helpful, and maintains a professional yet friendly tone. 
It directly addresses the customer's question with all relevant policy details.
```

---

## 💪 **Challenge Tips**

1. **Copy the Knowledge Base code** - Use the provided `KNOWLEDGE_BASE` and helper function
2. **Clear Agent Roles** - Each agent should have ONE specific job
3. **Test Incrementally** - Test each agent individually before building the full workflow
4. **Read Sample 4** - It's your blueprint for sequential workflows!
5. **Agent Communication** - Each agent receives full conversation history

---

## 🎉 **Bonus Ideas**

- Add sentiment analysis to detect frustration in complaints
- Include customer satisfaction scoring
- Support multi-language queries
- Add escalation logic for complex issues
- Create a feedback loop for continuous improvement

---

<div align="center">

**🌟 Ready to build your customer service pipeline? Let's go! 🌟**

</div>
