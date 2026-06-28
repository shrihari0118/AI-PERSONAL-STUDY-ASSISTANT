from pydantic import BaseModel, Field

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