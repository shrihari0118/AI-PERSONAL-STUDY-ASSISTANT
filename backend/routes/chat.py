from fastapi import APIRouter
from pydantic import BaseModel

from services.llm_service import generate_response

router = APIRouter()

class ChatRequest(BaseModel):
    message : str

@router.post("/chat")
def chat(request : ChatRequest):
    message = request.message
    answer = generate_response(message)
    return {
        "response" : answer
    }
