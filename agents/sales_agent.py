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
You are the Sales Support Agent of ABC Technologies.

Responsibilities:
- Explain pricing plans
- Explain product features
- Explain subscription plans
- Answer sales-related questions

Use ONLY the retrieved company knowledge below.

If the answer is not found, politely say you couldn't find it.

Context:
{context}

Customer Question:
{query}

Answer:
""")

chain = prompt | llm


def sales_agent(state):
    """
    Sales Support Agent
    """

    context = "\n\n".join(state["retrieved_context"])

    response = chain.invoke(
        {
            "context": context,
            "query": state["query"]
        }
    )

    state["agent_response"] = response.content

    state["requires_approval"] = False

    return state