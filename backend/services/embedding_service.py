from sentence_transformers import SentenceTransformer
from backend.schemas.chunk import Chunk
from backend.schemas.embedding import EmbeddedChunk

# Load the embedding model once during application startup.
MODEL = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def generate_embeddings(chunks : list[Chunk]) -> list[EmbeddedChunk]:
    if not chunks:
        return []
    
    texts = [
        chunk.text
        for chunk in chunks
    ]

    embeddings = MODEL.encode(texts, convert_to_numpy=True)

    embedded_chunks = []

    for chunk, embedding in zip(chunks, embeddings):
        embedded_chunk = EmbeddedChunk(
            chunk_id = chunk.chunk_id,
            text = chunk.text,
            embedding = embedding.tolist()
        )

        embedded_chunks.append(embedded_chunk)

    return embedded_chunks

def generate_query_embeddings(question : str) -> list[float]:
    if not question.strip():
        raise ValueError("Question cannot be empty")

    embedding = MODEL.encode(question, convert_to_numpy = True)
    return embedding.tolist()

