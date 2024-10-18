# tests/test_api.py

from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the LLAMA 3.1 API"}

def test_query_model():
    response = client.post("/api/query", json={"question": "What is the capital of France?"})
    assert response.status_code == 200
    assert "response" in response.json()
    assert "<div class=\"llama-response\">" in response.json()["response"]

def test_query_model_invalid_input():
    response = client.post("/api/query", json={})
    assert response.status_code == 422  # Unprocessable Entity

def test_query_model_server_error(mocker):
    # Mock the LlamaWrapper to raise an exception
    mocker.patch("src.model.llama_wrapper.LlamaWrapper.generate", side_effect=Exception("Model error"))
    
    response = client.post("/api/query", json={"question": "This will cause an error"})
    assert response.status_code == 500
    assert "detail" in response.json()
