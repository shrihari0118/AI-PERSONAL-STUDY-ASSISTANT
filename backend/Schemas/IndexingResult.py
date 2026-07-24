from pydantic import BaseModel

class IndexingResult(BaseModel):
    success : bool
    message : str
    chunks_created : int
    embeddings_stored : int