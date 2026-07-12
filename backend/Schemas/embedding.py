from pydantic import BaseModel

class EmbeddedChunk(BaseModel):
    chunk_id: int
    text: str
    embedding: list[float]