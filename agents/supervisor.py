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
You are the Customer Support Supervisor of ABC Technologies.

Review and improve the support agent's response.

Rules:
- Improve grammar and clarity.
- Make the response professional and customer-friendly.
- Ensure it follows company policy.
- Do NOT change the meaning.
- Do NOT invent new information.
- NEVER explain what you changed.
- NEVER mention that you reviewed or improved the response.
- Return ONLY the final customer response.

Customer Question:
{query}

Agent Response:
{response}

Final Customer Response:
""")

chain = prompt | llm


def supervisor(state):
    """
    Review and improve the final response.
    """

    response = chain.invoke(
        {
            "query": state["query"],
            "response": state["agent_response"]
        }
    )

    state["final_response"] = response.content

    return state