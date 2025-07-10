from fastapi import APIRouter
from app.services.rag import ask_question

router = APIRouter()

@router.get("/ask")
async def ask(query: str):
    result = await ask_question(query)
    return {"answer": result}
