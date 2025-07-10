
```
# 📊 Financial RAG: Ask Questions from Financial PDFs using LangChain, OpenAI & FastAPI

A lightweight Retrieval-Augmented Generation (RAG) app that lets you ask natural language questions from financial PDFs like annual reports and get accurate answers using OpenAI’s language models and FAISS vector search.

---

## 🚀 Features

- 🔍 PDF parsing and chunking
- 🧠 Embedding with OpenAI
- 📚 FAISS vector store for retrieval
- 🌐 FastAPI-powered backend API
- ✅ Ask questions like: “What was Tesla’s 2023 revenue?”

---

## ⚙️ Requirements

- Python 3.10+
- OpenAI API Key

Install dependencies:

```bash
pip install -r requirements.txt
````

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_key_here
```

---

## 📥 Ingest a PDF

Put your PDF file in the root directory (e.g., `tesla_2023.pdf`) and run:

```bash
python ingest_runner.py
```

This will:

* Load the PDF
* Chunk it
* Generate embeddings
* Save a FAISS vector store to disk

---

## 🚀 Run the API Server

```bash
uvicorn main:app --reload
```

Open your browser and go to:

```
http://localhost:8000/docs
```

Use the `/ask` endpoint like this:

```
GET /ask?query=what is tesla revenue?
```

---

## ✅ Example Output

```json
{
  "answer": "Tesla's total revenue for the year ended December 31, 2023, was $96,773 million."
}
```


