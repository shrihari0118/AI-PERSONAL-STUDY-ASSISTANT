from backend.schemas.retrieval import RetrievalResult
from backend.services.embedding_service import generate_query_embeddings

def retrieve_answer(question : str) -> RetrievalResult:
    query_embedding = generate_query_embeddings(question)

    return RetrievalResult(
        answer = "Query embedding generated successfully",
        retrieved_chunks = 0
    )