import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# Load environment variables from .env file
load_dotenv()

def ingest_documents(pdf_path: str, persist_path: str = "vector_store"):
    # Step 1: Load PDF
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    # Step 2: Split text into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    # Step 3: Embed chunks
    embeddings = OpenAIEmbeddings(
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # Step 4: Save vectorstore
    vectorstore.save_local(persist_path)
    print(f"✅ Ingestion complete. Vector DB saved to: {persist_path}")
