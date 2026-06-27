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
You are the Account Support Agent of ABC Technologies.

Responsibilities:
- Password reset
- Profile updates
- Account activation
- Account deactivation
- Account closure

Use ONLY the retrieved company knowledge below.

If the answer is not found, politely say you couldn't find it.

Context:
{context}

Customer Question:
{query}

Answer:
""")

chain = prompt | llm


def account_agent(state):
    """
    Account Support Agent
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
        "close account",
        "account closure",
        "delete account",
        "deactivate permanently"
    ]

    state["requires_approval"] = any(
        keyword in query for keyword in approval_keywords
    )

    return state