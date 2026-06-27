from pathlib import Path

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


CHROMA_DB_DIR = Path("rag/chroma_db")


def get_retriever():
    """
    Load the existing Chroma vector database and return a retriever.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma(
        persist_directory=str(CHROMA_DB_DIR),
        embedding_function=embeddings
    )

    return vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )