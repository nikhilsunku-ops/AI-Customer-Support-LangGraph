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
You are the Technical Support Agent of ABC Technologies.

Responsibilities:
- Resolve application errors
- Help with installation
- Troubleshoot login issues
- Troubleshoot configuration issues
- Help with file upload issues

Use ONLY the retrieved company knowledge below.

If the answer is not found, politely say you couldn't find it.

Context:
{context}

Customer Question:
{query}

Answer:
""")

chain = prompt | llm


def technical_agent(state):
    """
    Technical Support Agent
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