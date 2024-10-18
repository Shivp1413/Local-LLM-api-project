# src/api/routes.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..model.llama_wrapper import LlamaWrapper
from ..utils.html_formatter import format_to_html

router = APIRouter()
llama_model = LlamaWrapper()

class Query(BaseModel):
    question: str

@router.post("/api/query")
async def query_model(query: Query):
    try:
        response = llama_model.generate(query.question)
        html_response = format_to_html(response)
        return {"response": html_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
