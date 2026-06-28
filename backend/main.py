from fastapi import FastAPI
from routes.chat_route import router as chat_router
from routes.documents import router as document_router

app = FastAPI()

@app.get("/")
def home():
    return {"message" : "AI personal study assistant is running"}

@app.get("/ask")
def ask(question : str):
    return {"question" : question}

app.include_router(chat_router)
app.include_router(document_router)