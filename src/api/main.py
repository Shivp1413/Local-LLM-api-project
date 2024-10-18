# src/api/main.py

from fastapi import FastAPI
from .routes import router

app = FastAPI(title="LLAMA 3.1 API", description="API for querying LLAMA 3.1 model")

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to the LLAMA 3.1 API"}
