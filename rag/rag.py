from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from rag.retriever import get_retriever
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model=os.getenv("MODEL_NAME"),
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

prompt = ChatPromptTemplate.from_template("""
You are an AI Customer Support Assistant for ABC Technologies.

Use ONLY the information provided in the context below to answer the customer's question.

If the answer is not available in the context, politely say:

"I couldn't find that information in the company knowledge base."

Context:
{context}

Customer Question:
{question}

Answer:
""")


def rag_response(question: str):
    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    chain = prompt | llm

    response = chain.invoke({
        "context": context,
        "question": question
    })

    return response.content