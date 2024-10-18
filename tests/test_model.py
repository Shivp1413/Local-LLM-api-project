# tests/test_model.py

import pytest
from src.model.llama_wrapper import LlamaWrapper

@pytest.fixture
def llama_model():
    return LlamaWrapper()

def test_llama_wrapper_initialization(llama_model):
    assert llama_model.model == "llama:3.1"

def test_llama_wrapper_generate(llama_model, mocker):
    # Mock the ollama.generate function
    mock_generate = mocker.patch("ollama.generate")
    mock_generate.return_value = {"response": "This is a test response."}

    response = llama_model.generate("Test prompt")
    
    assert response == "This is a test response."
    mock_generate.assert_called_once_with(model="llama:3.1", prompt="Test prompt")

def test_llama_wrapper_generate_error(llama_model, mocker):
    # Mock the ollama.generate function to raise an exception
    mock_generate = mocker.patch("ollama.generate", side_effect=Exception("Model error"))

    with pytest.raises(Exception) as exc_info:
        llama_model.generate("Test prompt")
    
    assert str(exc_info.value) == "Model error"
