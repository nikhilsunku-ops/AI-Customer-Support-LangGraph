def route_department(state):
    """
    Route the query to the correct department.
    """

    intent = state["intent"]

    routes = {
    "Sales": "sales_agent",
    "Technical": "technical_agent",
    "Billing": "billing_agent",
    "Account": "account_agent",
    "Memory": "memory_node"
}

    return routes.get(intent, "supervisor")
def route_approval(state):
    """
    Decide whether human approval is required.
    """

    if state["requires_approval"]:
        return "human_approval"

    return "supervisor"