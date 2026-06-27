from dotenv import load_dotenv
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model=os.getenv("MODEL_NAME"),
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

prompt = ChatPromptTemplate.from_template("""
You are the Billing Support Agent of ABC Technologies.

Responsibilities:
- Answer billing questions
- Explain invoices
- Explain payments
- Handle refund requests
- Handle subscription cancellation requests

Use ONLY the retrieved company knowledge below.

If the answer is not found, politely say you couldn't find it.

Context:
{context}

Customer Question:
{query}

Answer:
""")

chain = prompt | llm


def billing_agent(state):
    """
    Billing Support Agent
    """

    context = "\n\n".join(state["retrieved_context"])

    response = chain.invoke(
        {
            "context": context,
            "query": state["query"]
        }
    )

    state["agent_response"] = response.content

    query = state["query"].lower()

    approval_keywords = [
        "refund",
        "cancel subscription",
        "subscription cancellation",
        "compensation",
        "escalation",
        "manager"
    ]

    state["requires_approval"] = any(
        keyword in query for keyword in approval_keywords
    )

    return state