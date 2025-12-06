Below is a **clean, professional, production-quality README.md** for your **Knowledge-Base Search Engine** repository using **ChromaDB + LangChain + Groq + FastAPI + Streamlit + Context-Aware RAG + Re-ranking**.

You can copy-paste this directly into your GitHub repo.

---

# 🚀 Knowledge-Base Search Engine (RAG + ChromaDB + Groq + LangChain)

An end-to-end **Retrieval Augmented Generation (RAG)** system that ingests PDF/Text documents and answers user queries using:

* **ChromaDB** (local vector DB)
* **LangChain** (retrievers, history-aware query rewriting, pipelines)
* **Groq LLM** (LLaMA-3.1-8B Instant)
* **FastAPI** backend
* **Streamlit** frontend
* **Re-ranking + Context-Aware Retrieval**
* **Virtual environment support**

This project provides a clean, simple, and scalable RAG architecture suitable for knowledge-base search, report automation, and enterprise document Q&A.

---

# 📌 Features

### ✅ Document Ingestion

* Upload PDFs or text files
* Chunking using LangChain text splitters
* Embedding using **SentenceTransformers (MiniLM-L6-v2)**
* Stored inside **ChromaDB**

### ✅ Query Engine

* Context-aware query rewriting
* Multi-step RAG
* Re-ranking of retrieved chunks
* Final answer generated using **Groq LLM**

### ✅ Frontend + Backend

* **FastAPI** backend for ingestion + query
* **Streamlit UI** for chat-based querying
* Real-time responses
* Stores and uses conversation history

---

# 🧩 Tech Stack

| Component       | Technology                              |
| --------------- | --------------------------------------- |
| LLM             | Groq (LLaMA-3.1-8B-Instant)             |
| Vector DB       | ChromaDB                                |
| Embeddings      | all-MiniLM-L6-v2 (SentenceTransformers) |
| Backend         | FastAPI                                 |
| Frontend        | Streamlit                               |
| Orchestration   | LangChain                               |
| Re-ranking      | LLM-based                               |
| Query Rewriting | History-aware                           |

---

# 📂 Project Structure

```
Knowlwdge_Base_Search_Engine/
│── backend/
│     ├── app.py
│     ├── rag.py
│     ├── ingest.py
│     ├── requirements.txt
│── chroma_db/            ← auto-created after ingestion
│── data/                 ← place PDFs/TXT here
│── streamlit_app.py
│── .env
│── venv/                 ← python virtual environment
```

---

# 🔧 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Knowledge_Base_Search_Engine.git
cd Knowledge_Base_Search_Engine
```

---

# 🐍 2️⃣ Create & Activate Virtual Environment (Recommended)

### Windows (PowerShell):

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 📦 3️⃣ Install Required Packages

```bash
pip install -r backend/requirements.txt
```

Or manually:

```
pip install langchain langchain-community langchain-text-splitters langchain-groq chromadb pypdf python-dotenv fastapi uvicorn streamlit requests sentence-transformers
```

---

# 🔑 4️⃣ Setup Environment Variables

Create a `.env` file in project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get your free key from: [https://console.groq.com/keys](https://console.groq.com/keys)

---

# 📥 5️⃣ Add Your Documents

Place `.pdf` or `.txt` files inside:

```
/data/
```

Example:

```
data/myfile.pdf
data/notes.txt
```

---

# 🧠 6️⃣ Run Document Ingestion (Creates ChromaDB)

```bash
cd backend
python ingest.py
```

You should now see a **chroma_db/** folder created.

---

# 🚀 7️⃣ Run FastAPI Backend

```bash
uvicorn app:app --reload
```

Backend runs at:

👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

# 🖥️ 8️⃣ Run Streamlit Frontend

Open a new terminal (keep backend running):

```bash
streamlit run streamlit_app.py
```

Streamlit UI starts at:

👉 [http://localhost:8501](http://localhost:8501)

---

# 🧪 Test Your RAG System

Ask:

```
"What is covered in document X?"
```

or

```
"Summarize the key points."
```

Follow-up context-aware queries also work:

```
"Explain more."
"Give an example."
"Why is that important?"
```

---

# 🛠 How It Works (RAG Pipeline)

1. **Query Rewriting**
   LangChain rewrites user query based on chat history.

2. **Vector Search**
   Improved query → ChromaDB → top-k document chunks.

3. **Re-Ranking**
   Groq LLM ranks chunks → selects best relevant ones.

4. **Answer Generation**
   RAG prompt + reranked text → Groq LLM → final answer.

---

# 📹 Demo Video

> Upload your demo video and add link here.

---

# 📚 API Endpoints

### `POST /ingest`

Load all documents from `data/` into ChromaDB.

### `POST /query`

Send a query + history → returns a RAG answer.

---

# 🤝 Contributing

Pull requests and improvements are welcome!

---

# 📝 License

MIT License

---

# ⭐ Support

If you like this project, please ⭐ the repository!

---

If you want, I can also generate:

✅ a **perfect README banner image**,
✅ a **project logo**,
✅ **GitHub Wiki documentation**,
or
✅ a **PDF project report**.

Just tell me!
