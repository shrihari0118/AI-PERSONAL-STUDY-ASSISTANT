from pydantic import BaseModel

class RetrievalResult(BaseModel):
    answer : str
    retrieved_chunks : int