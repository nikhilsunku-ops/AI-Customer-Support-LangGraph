from langgraph.graph import StateGraph, END

from state import CustomerSupportState

from agents.classifier import classify_intent
from agents.sales_agent import sales_agent
from agents.technical_agent import technical_agent
from agents.billing_agent import billing_agent
from agents.account_agent import account_agent
from agents.supervisor import supervisor
from agents.human_approval import human_approval
from memory.memory_node import memory_node
from router import route_department, route_approval


workflow = StateGraph(CustomerSupportState)

# -------------------------
# Nodes
# -------------------------

workflow.add_node("classifier", classify_intent)

workflow.add_node("sales_agent", sales_agent)

workflow.add_node("technical_agent", technical_agent)

workflow.add_node("billing_agent", billing_agent)

workflow.add_node("account_agent", account_agent)

workflow.add_node("human_approval", human_approval)

workflow.add_node("supervisor", supervisor)

workflow.add_node("memory_node", memory_node)

# -------------------------
# Entry Point
# -------------------------

workflow.set_entry_point("classifier")

# -------------------------
# Intent Routing
# -------------------------

workflow.add_conditional_edges(
    "classifier",
    route_department,
    {
        "sales_agent": "sales_agent",
        "technical_agent": "technical_agent",
        "billing_agent": "billing_agent",
        "account_agent": "account_agent",
        "memory_node": "memory_node"
    }
)

# -------------------------
# Sales
# -------------------------

workflow.add_conditional_edges(
    "sales_agent",
    route_approval,
    {
        "human_approval": "human_approval",
        "supervisor": "supervisor"
    }
)

# -------------------------
# Technical
# -------------------------

workflow.add_conditional_edges(
    "technical_agent",
    route_approval,
    {
        "human_approval": "human_approval",
        "supervisor": "supervisor"
    }
)

# -------------------------
# Billing
# -------------------------

workflow.add_conditional_edges(
    "billing_agent",
    route_approval,
    {
        "human_approval": "human_approval",
        "supervisor": "supervisor"
    }
)

# -------------------------
# Account
# -------------------------

workflow.add_conditional_edges(
    "account_agent",
    route_approval,
    {
        "human_approval": "human_approval",
        "supervisor": "supervisor"
    }
)

# -------------------------
# Human Approval
# -------------------------

workflow.add_edge(
    "human_approval",
    "supervisor"
)

# -------------------------
# End
# -------------------------

workflow.add_edge(
    "supervisor",
    "memory_node"
)

workflow.add_edge(
    "memory_node",
    END
)

graph = workflow.compile()