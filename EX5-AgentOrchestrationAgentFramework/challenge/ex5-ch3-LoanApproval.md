# 💰 Challenge 3: Loan Approval System with Conditional Branching

<div align="center">

![Challenge 3](https://img.shields.io/badge/Challenge-3-blue?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Difficulty-Advanced-red?style=for-the-badge)
![Time](https://img.shields.io/badge/Time-40%20minutes-orange?style=for-the-badge)

**Build a complex workflow with branching logic, loops, and multiple decision paths!**

</div>

---

## 🎯 **Objective**

Create a **sophisticated loan approval workflow** using `WorkflowBuilder` with conditional branching, multiple decision points, and iterative improvement loops - simulating a real financial approval system!

## ✨ **What You'll Learn**

<table>
<tr>
<td>

### 🔄 **Core Skills**
- Building complex graph-based workflows
- Implementing conditional routing
- Creating feedback loops
- Managing multi-path execution

</td>
<td>

### 🧠 **AI Concepts**  
- WorkflowBuilder advanced patterns
- Conditional edge conditions
- Pydantic structured outputs
- Multi-agent decision systems

</td>
</tr>
</table>

---

## 📝 **Challenge Description**

Based on **Sample 5** (`ex5-s5-WorkflowBuilder.py`), create a loan approval system with multiple specialized agents and complex branching logic:

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; margin: 15px 0; color: white;">

### 🎯 **Your Mission**

**Create a multi-path loan approval workflow:**

```
Application → Credit Scorer → [Good Credit] → Amount Validator → [Within Limits] → Approver
                            ↓                                    ↓
                      [Poor Credit]                      [Exceeds Limits]
                            ↓                                    ↓
                   Manual Reviewer ←──────────────────────────┘
                            ↓
                  [Approved with Conditions] → Document Verifier → [Complete] → Approver
                            ↓                                      ↓
                      [Rejected]                              [Incomplete]
                            ↓                                      ↓
                    Rejection Handler                    Applicant (loop back)
```

**🌟 Goal**: Build a realistic financial approval system with multiple decision points!

</div>

---

## 🛠️ **Loan Application Data - Starter Code**

<div style="background: #e7f3ff; padding: 15px; border-radius: 8px; border-left: 4px solid #0066cc; margin: 10px 0;">

**📦 Use this data model for loan applications:**

```python
from pydantic import BaseModel
from typing import List, Optional

class LoanApplication(BaseModel):
    """Loan application data structure."""
    applicant_name: str
    loan_amount: float
    annual_income: float
    credit_score: int  # 300-850
    employment_years: int
    existing_debts: float
    loan_purpose: str

class CreditAssessment(BaseModel):
    """Credit scoring results."""
    credit_score: int
    risk_level: str  # low, medium, high
    decision: str  # auto_approve, manual_review, reject
    reason: str
    application: LoanApplication

class AmountValidation(BaseModel):
    """Loan amount validation results."""
    loan_amount: float
    annual_income: float
    debt_to_income_ratio: float
    within_limits: bool
    decision: str  # approve, manual_review
    reason: str
    application: LoanApplication

class ManualReview(BaseModel):
    """Manual review decision."""
    approved: bool
    conditions: Optional[List[str]] = None
    reason: str
    application: LoanApplication

class DocumentCheck(BaseModel):
    """Document verification results."""
    complete: bool
    missing_documents: List[str]
    application: LoanApplication

class FinalDecision(BaseModel):
    """Final loan decision."""
    approved: bool
    loan_amount: float
    interest_rate: float
    conditions: List[str]
    message: str

# Helper function to create test applications
def create_test_application(
    name: str,
    amount: float,
    income: float,
    credit_score: int,
    employment_years: int = 5,
    existing_debts: float = 5000,
    purpose: str = "home_improvement"
) -> LoanApplication:
    """Create a test loan application."""
    return LoanApplication(
        applicant_name=name,
        loan_amount=amount,
        annual_income=income,
        credit_score=credit_score,
        employment_years=employment_years,
        existing_debts=existing_debts,
        loan_purpose=purpose
    )

# Test scenarios
TEST_SCENARIOS = {
    "excellent": create_test_application("John Doe", 50000, 120000, 780),
    "good": create_test_application("Jane Smith", 30000, 80000, 720),
    "medium": create_test_application("Bob Johnson", 40000, 60000, 650),
    "risky": create_test_application("Alice Brown", 60000, 50000, 580),
    "poor": create_test_application("Charlie Wilson", 70000, 45000, 520)
}
```

**💡 Credit Score Ranges:**
- **Excellent**: 750+ (auto-approve path)
- **Good**: 700-749 (auto-approve with validation)
- **Fair**: 650-699 (manual review likely)
- **Poor**: 600-649 (manual review required)
- **Very Poor**: <600 (high risk, strict review)

</div>

---

## 📋 **Technical Requirements**

### 🥇 **Basic Level (30-35 minutes)** ✅ MAIN GOAL

<div style="background: #d4edda; padding: 15px; border-radius: 8px; border-left: 4px solid #28a745; margin: 10px 0;">

**Build the core workflow with conditional branching!**

- [ ] ✅ **Credit Scorer Agent**: Evaluates credit score and risk level
  - Returns `CreditAssessment` with decision
  - Routes to: auto_approve, manual_review, or reject

- [ ] ✅ **Amount Validator Agent**: Checks loan-to-income ratio
  - Validates if amount is within safe limits (max 4x annual income)
  - Calculates debt-to-income ratio
  - Routes to: approve or manual_review

- [ ] ✅ **Manual Reviewer Agent**: Human-like review decision
  - Evaluates borderline cases
  - Can approve with conditions or reject
  - Returns `ManualReview` decision

- [ ] ✅ **Approver Agent**: Final approval with terms
  - Determines interest rate based on risk
  - Sets loan conditions
  - Returns `FinalDecision`

- [ ] ✅ **Conditional Routing**: Implement edge conditions for branching
  - Good credit → Amount Validator
  - Poor credit → Manual Reviewer
  - Within limits → Approver
  - Exceeds limits → Manual Reviewer

- [ ] ✅ **Test Scenarios**: Test with at least 3 different credit profiles

</div>

### 🌟 **Advanced Level (Extra 10-15 minutes)** ⭐ BONUS

<div style="background: #fff3cd; padding: 15px; border-radius: 8px; border-left: 4px solid #ffc107; margin: 10px 0;">

**Add document verification loop and rejection handling!**

- [ ] 🔥 **Document Verifier Agent**: Checks required documents
  - Returns `DocumentCheck` with completeness status
  - Routes to: Approver (complete) or Applicant loop (incomplete)

- [ ] 🔥 **Rejection Handler**: Processes rejections professionally
  - Provides clear reasons
  - Suggests improvements
  - Offers reapplication guidance

- [ ] 🔥 **Applicant Loop**: Document resubmission cycle
  - Loops back to Document Verifier
  - Max 2 iterations
  - Clear console output showing loop

- [ ] 🔥 **Console Progress**: Show decision path in real-time (like Sample 5)

</div>

---

## 💡 **Getting Started Hints**

### 🟢 **Basic Level Implementation**

<details>
<summary><b>💡 Hint 1: Credit Scorer Agent with Structured Output</b></summary>

```python
credit_scorer = AgentExecutor(
    chat_client.create_agent(
        instructions=(
            "You are a credit risk assessor. Analyze the loan application: "
            "- Excellent (750+): auto_approve "
            "- Good (700-749): auto_approve "
            "- Fair (650-699): manual_review "
            "- Poor (600-649): manual_review "
            "- Very Poor (<600): reject "
            "Return JSON with credit_score, risk_level, decision, reason, and application."
        ),
        response_format=CreditAssessment,
    ),
    id="credit_scorer"
)
```

</details>

<details>
<summary><b>💡 Hint 2: Conditional Edge Functions</b></summary>

Create condition functions for routing:

```python
def auto_approve_condition(message: Any) -> bool:
    """Route to amount validator if auto-approved."""
    if not isinstance(message, AgentExecutorResponse):
        return True
    try:
        assessment = CreditAssessment.model_validate_json(
            message.agent_run_response.text
        )
        return assessment.decision == "auto_approve"
    except:
        return False

def manual_review_condition(message: Any) -> bool:
    """Route to manual reviewer if needed."""
    # Similar pattern...
    
def reject_condition(message: Any) -> bool:
    """Route to rejection handler."""
    # Similar pattern...
```

</details>

<details>
<summary><b>💡 Hint 3: WorkflowBuilder with Branching</b></summary>

Build the graph with conditional edges:

```python
workflow = (
    WorkflowBuilder(
        name="Loan Approval System",
        description="Multi-path loan approval with conditional routing"
    )
    .set_start_executor(credit_scorer)
    # Branch based on credit assessment
    .add_edge(credit_scorer, amount_validator, condition=auto_approve_condition)
    .add_edge(credit_scorer, manual_reviewer, condition=manual_review_condition)
    .add_edge(credit_scorer, rejection_handler, condition=reject_condition)
    # Amount validation branches
    .add_edge(amount_validator, approver, condition=within_limits_condition)
    .add_edge(amount_validator, manual_reviewer, condition=exceeds_limits_condition)
    # Manual review branches
    .add_edge(manual_reviewer, approver, condition=approved_condition)
    .add_edge(manual_reviewer, rejection_handler, condition=rejected_condition)
    # Final outputs
    .add_edge(approver, final_output_executor)
    .add_edge(rejection_handler, final_output_executor)
    .build()
)
```

</details>

<details>
<summary><b>💡 Hint 4: Test with Different Profiles</b></summary>

```python
# Test excellent credit
app1 = TEST_SCENARIOS["excellent"]  # Should auto-approve

# Test risky application  
app2 = TEST_SCENARIOS["risky"]  # Should go to manual review

# Test poor credit
app3 = TEST_SCENARIOS["poor"]  # Should be rejected
```

</details>

### 🔥 **Advanced Level Implementation**

<details>
<summary><b>💡 Hint 5: Document Verification Loop</b></summary>

Add document loop after manual approval:

```python
# Add document verifier after manual reviewer
.add_edge(manual_reviewer, document_verifier, condition=approved_with_conditions)

# Loop back if incomplete
.add_edge(document_verifier, applicant_resubmit, condition=incomplete_condition)
.add_edge(applicant_resubmit, document_verifier)

# Approve if complete
.add_edge(document_verifier, approver, condition=complete_condition)
```

Track iterations to prevent infinite loops!

</details>

<details>
<summary><b>💡 Hint 6: Real-time Progress Display</b></summary>

Add console output in condition functions:

```python
def auto_approve_condition(message: Any) -> bool:
    if not isinstance(message, AgentExecutorResponse):
        return True
    try:
        assessment = CreditAssessment.model_validate_json(...)
        if assessment.decision == "auto_approve":
            print(f"\n✅ Credit Score: {assessment.credit_score} - AUTO APPROVED")
            print(f"   Risk Level: {assessment.risk_level}")
            print(f"   → Routing to Amount Validator")
            return True
        return False
    except:
        return False
```

</details>

---

## 🎓 **Learning Resources**

### 📚 **Reference Samples**
- **Sample 5**: `ex5-s5-WorkflowBuilder.py` - Complete conditional branching example
- **Sample 6**: `ex5-s6-WorkflowDevUI.py` - Workflow visualization (optional)

### 🔗 **Key Concepts**
- **WorkflowBuilder**: Low-level graph control
- **Conditional Edges**: `condition=` parameter in `add_edge()`
- **Pydantic Models**: `response_format=` for structured outputs
- **Custom Executors**: `@executor` decorator for transformations

---

## ✅ **Success Criteria**

### Basic Level
- ✅ 4 core agents with clear roles (Credit Scorer, Amount Validator, Manual Reviewer, Approver)
- ✅ Conditional routing works for all decision points
- ✅ Credit score-based branching (auto-approve vs manual vs reject)
- ✅ Amount validation branching (within limits vs exceeds)
- ✅ Structured outputs with Pydantic models
- ✅ Successfully tested with 3+ different credit profiles
- ✅ Clear console output showing decision path

### Advanced Level  
- ✅ Document verification loop implemented
- ✅ Rejection handler processes denials professionally
- ✅ Applicant resubmission loop with iteration limits
- ✅ Real-time progress display (like Sample 5)
- ✅ All test scenarios produce expected paths
- ✅ Code is well-documented and maintainable

---

## 🚀 **Expected Output**

### Example Execution - Excellent Credit
```
🏦 LOAN APPROVAL SYSTEM
================================================================================

📝 Processing Application: John Doe
   Loan Amount: $50,000
   Annual Income: $120,000
   Credit Score: 780

💳 Credit Scorer Review:
   Score: 780 (Excellent)
   Risk Level: LOW
   Decision: ✅ AUTO APPROVE - Routing to Amount Validator

💰 Amount Validator:
   Loan-to-Income Ratio: 0.42 (42%)
   Debt-to-Income Ratio: 0.12 (12%)
   Decision: ✅ WITHIN SAFE LIMITS - Routing to Approver

✅ Final Decision: APPROVED
   Loan Amount: $50,000
   Interest Rate: 3.5%
   Conditions: []
   Message: Congratulations! Your loan has been approved with excellent terms.
```

### Example Execution - Manual Review Required
```
📝 Processing Application: Alice Brown
   Loan Amount: $60,000
   Annual Income: $50,000
   Credit Score: 580

💳 Credit Scorer Review:
   Score: 580 (Poor)
   Risk Level: HIGH
   Decision: ⚠️ MANUAL REVIEW REQUIRED

👤 Manual Reviewer:
   Overall Assessment: Borderline case
   Decision: ✅ APPROVED WITH CONDITIONS
   Conditions: ["Co-signer required", "Higher interest rate", "Proof of employment"]
   → Routing to Document Verifier

📄 Document Verifier:
   Status: ❌ INCOMPLETE
   Missing: ["Employment verification", "Co-signer agreement"]
   → Routing back to Applicant for resubmission

🔄 Applicant: Resubmitting documents (Attempt 1/2)...

📄 Document Verifier:
   Status: ✅ COMPLETE
   → Routing to Approver

✅ Final Decision: APPROVED WITH CONDITIONS
   Loan Amount: $60,000
   Interest Rate: 8.5%
   Conditions: ["Co-signer required", "Higher down payment"]
```

---

## 💪 **Challenge Tips**

1. **Start with Sample 5** - It's your complete blueprint!
2. **Draw the Flow** - Sketch the decision tree before coding
3. **Test Incrementally** - Test each branch separately
4. **Use Structured Outputs** - Pydantic models make routing reliable
5. **Console Output** - Add prints in condition functions (like Sample 5)
6. **Iterate Limit** - Add loop counters to prevent infinite cycles

---

## 🎉 **Bonus Ideas**

- Add co-signer evaluation path
- Include collateral assessment for secured loans
- Implement appeal process for rejections
- Add A/B testing for different approval thresholds
- Create DevUI visualization of the workflow graph
- Export approval metrics and statistics

---

<div align="center">

**🌟 Ready to build your loan approval system? Let's go! 🌟**

</div>
