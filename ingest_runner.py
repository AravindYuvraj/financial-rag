# ingest_runner.py

from app.services.ingest import ingest_documents

if __name__ == "__main__":
    ingest_documents("tesla_2023.pdf")
