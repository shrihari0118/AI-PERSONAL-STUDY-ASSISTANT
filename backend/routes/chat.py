from fastapi import APIRouter
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse

from services.llm_service import generate_response

router = APIRouter()

class ChatRequest(BaseModel):
    message : str = Field(
        ...,
        min_length = 1,
        description = "User message for the AI Assistant"
    )

class ChatResponse(BaseModel):
    success : bool
    response : str | None = None
    error : str | None = None

@router.post("/chat", response_model = ChatResponse)
def chat(request : ChatRequest):
    try:
        answer = generate_response(request.message)

        return ChatResponse(
            success = True,
            response = answer,
            error = None
        )
    except Exception as e:
        print(f"LLM Error: {e}")
        return JSONResponse(
            status_code = 500,
            content = {
                "success" : False,
                "response" : None,
                "error" : "AI service is temporarily unavailable"
            }
        )