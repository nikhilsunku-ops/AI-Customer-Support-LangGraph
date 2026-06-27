from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


DOCUMENTS_DIR = Path("documents")


def load_documents():
    """
    Load all PDF documents from the documents folder.
    """

    documents = []

    for pdf_file in DOCUMENTS_DIR.glob("*.pdf"):
        loader = PyPDFLoader(str(pdf_file))
        documents.extend(loader.load())

    return documents