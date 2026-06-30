from fastapi import APIRouter
from backend.schemas.chat import ChatRequest, ChatResponse
from fastapi.responses import JSONResponse

from backend.services.llm_service import generate_response

router = APIRouter()

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