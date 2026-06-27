from typing import TypedDict, List, Optional


class CustomerSupportState(TypedDict):
    # Customer Information
    customer_name: Optional[str]
    customer_id: Optional[str]

    # User Query
    query: str

    # Intent Classification
    intent: Optional[str]
    department: Optional[str]

    # RAG
    retrieved_context: List[str]

    # Conversation Memory
    conversation_history: List[str]

    # Human Approval
    requires_approval: bool
    approval_status: Optional[str]

    # Agent Responses
    agent_response: Optional[str]
    final_response: Optional[str]

    # Workflow Control
    next_node: Optional[str]

    # Error Handling
    error: Optional[str]