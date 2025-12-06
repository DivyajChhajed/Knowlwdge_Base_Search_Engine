import streamlit as st
import requests

st.title("📘 Simple RAG Search Engine (Chroma + Groq)")

query = st.text_input("Ask something:")

if st.button("Search"):
    res = requests.post("http://localhost:8000/query", params={"query": query})
    st.write("### Answer:")
    st.write(res.json()["answer"])
