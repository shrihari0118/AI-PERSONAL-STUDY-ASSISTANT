import chromadb
from backend.schemas.embedding import EmbeddedChunk
from backend.config import CHROMA_DB_DIR

CLIENT = chromadb.PersistentClient(CHROMA_DB_DIR)

COLLECTION_NAME = "study_documents"

COLLECTION = CLIENT.get_or_create_collection(
    name = COLLECTION_NAME
)

def store_embeddings(embedded_chunk : list[EmbeddedChunk]):
    if not embedded_chunk:
        raise ValueError("No embeddings provided for storage")

    ids = [
        chunk.chunk_id
        for chunk in embedded_chunk
    ]

    documents = [
        chunk.text
        for chunk in embedded_chunk
    ]

    embeddings = [
        chunk.embedding
        for chunk in embedded_chunk
    ]

    COLLECTION.add(
        ids = ids,
        documents = documents,
        embeddings = embeddings
    )
