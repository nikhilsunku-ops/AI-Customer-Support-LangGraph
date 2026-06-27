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
You are an intent classification system.

Classify the customer query into ONLY ONE of these categories:

- Sales
- Technical
- Billing
- Account
- Memory

Rules:

Sales:
- Pricing
- Subscription plans
- Product information
- Features

Technical:
- Application crash
- Installation
- Login problems
- Configuration
- Errors
- Upload issues

Billing:
- Invoice
- Payment
- Refund
- Subscription cancellation

Account:
- Password reset
- Profile update
- Account activation
- Account deactivation
- Account closure

Memory:
- Previous issue
- Conversation history
- Earlier discussion
- What did I ask before?

Return ONLY the category name.

Customer Query:
{query}
""")

chain = prompt | llm


def classify_intent(state):
    """
    Classify the customer's intent and update the state.
    """

    query = state["query"]

    intent = chain.invoke(
        {
            "query": query
        }
    ).content.strip()

    state["intent"] = intent
    state["department"] = intent

    return state