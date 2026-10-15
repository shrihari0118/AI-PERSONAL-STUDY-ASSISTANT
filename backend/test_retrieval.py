from backend.services.retrieval_service import retrieve_answer

result = retrieve_answer(
    "What is FastAPI ?"
)

print(result)