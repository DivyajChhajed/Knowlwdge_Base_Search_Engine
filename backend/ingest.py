import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

DATA_DIR = "../data/"
DB_DIR = "../chroma_db/"

def load_documents():
    docs = []
    for file in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, file)
        if file.endswith(".pdf"):
            loader = PyPDFLoader(path)
        else:
            loader = TextLoader(path)
        docs.extend(loader.load())
    return docs

def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_documents(docs)

def create_chroma(docs):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    Chroma.from_documents(docs, embeddings, persist_directory=DB_DIR)
    print("Chroma DB created!")

if __name__ == "__main__":
    docs = load_documents()
    chunks = split_docs(docs)
    create_chroma(chunks)
