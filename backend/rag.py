import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()

DB_DIR = "../chroma_db/"

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

def history_aware_query(history, query):
    system_msg = (
        "You are a query rewriting assistant.\n"
        "Use the chat history and the new question to form a better query.\n"
        f"History: {history}\n"
        f"Question: {query}\n"
        "Return only the improved query text."
    )
    improved = llm.invoke(system_msg)
    return improved.content

def rerank(query, docs):
    text_block = "\n\n---\n\n".join([d.page_content for d in docs])
    msg = f"""
    Rank the following chunks by relevance to the query.
    Query: {query}
    Chunks:
    {text_block}
    Return ONLY the best 2 chunks merged together.
    """
    result = llm.invoke(msg)
    return result.content

def rag_answer(history, query):
    better_query = history_aware_query(history, query)
    docs = vectorstore.similarity_search(better_query, k=5)

    reranked_text = rerank(better_query, docs)

    final_prompt = f"""
    Using the following retrieved information, answer the user's question.

    Retrieved Text:
    {reranked_text}

    User Question:
    {query}
    """

    answer = llm.invoke(final_prompt)
    return answer.content
