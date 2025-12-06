from fastapi import FastAPI
from rag import rag_answer

app = FastAPI()
chat_history = []

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/query")
def ask(query: str):
    global chat_history
    answer = rag_answer(chat_history, query)
    chat_history.append({"user": query, "bot": answer})
    return {"answer": answer}
