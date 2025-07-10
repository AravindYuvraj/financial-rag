# app/services/rag.py

import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

load_dotenv()  # ✅ Load .env variables (including OPENAI_API_KEY)

VECTORSTORE_PATH = "vector_store"

async def ask_question(query: str) -> str:
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local(VECTORSTORE_PATH, embeddings, allow_dangerous_deserialization=True)
    
    retriever = db.as_retriever()
    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(temperature=0),
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=False,
    )

    result = qa.run(query)
    return result
