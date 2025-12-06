🚀 Knowledge-Base Search Engine (RAG + ChromaDB + Groq + LangChain)

An end-to-end Retrieval Augmented Generation (RAG) system that ingests PDF/Text documents and answers user queries using:

ChromaDB (local vector DB)

LangChain (retrievers, history-aware query rewriting, pipelines)

Groq LLM (LLaMA-3.1-8B Instant)

FastAPI backend

Streamlit frontend

Re-ranking + Context-Aware Retrieval

Virtual environment support

This project provides a clean, simple, and scalable RAG architecture suitable for knowledge-base search, report automation, and enterprise document Q&A.

📌 Features
✅ Document Ingestion

Upload PDFs or text files

Chunking using LangChain text splitters

Embedding using SentenceTransformers (MiniLM-L6-v2)

Stored inside ChromaDB

✅ Query Engine

Context-aware query rewriting

Multi-step RAG

Re-ranking of retrieved chunks

Final answer generated using Groq LLM

✅ Frontend + Backend

FastAPI backend for ingestion + query

Streamlit UI for chat-based querying

Real-time responses

Stores and uses conversation history
