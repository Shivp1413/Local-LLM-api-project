# LLAMA 3.1 API Project

## Overview

This project runs a LLAMA 3.1 language model locally on a Raspberry Pi using Ollama and provides an API for users and developers to create apps. The API accepts questions from users and provides outputs in HTML format.

## Features

- Local hosting of LLAMA 3.1 model on Raspberry Pi
- RESTful API for querying the model
- HTML-formatted responses
- Easy integration for developers to build applications

## Project Structure

```
llama-api-project/
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── routes.py
│   ├── model/
│   │   ├── __init__.py
│   │   └── llama_wrapper.py
│   └── utils/
│       ├── __init__.py
│       └── html_formatter.py
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   └── test_model.py
├── .gitignore
├── README.md
├── requirements.txt
└── setup.py
```

## Prerequisites

- Raspberry Pi (3 or newer recommended)/Windows/MAC
- Python 3.7+
- Ollama installed on the Raspberry Pi

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/Shivp1413/Local-LLM-api-project.git
   cd Local-LLM-api-project
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure Ollama is installed and the LLAMA 3.1 model is available:
   ```
   ollama pull llama:3.1
   ```

4. Run the API:
   ```
   uvicorn src.api.main:app --host 0.0.0.0 --port 8000
   ```

## Usage

To query the model, send a POST request to the `/api/query` endpoint:

```bash
curl -X POST "http://your-raspberry-pi-ip:8000/api/query" \
     -H "Content-Type: application/json" \
     -d '{"question": "What is the capital of France?"}'
```

The API will return an HTML-formatted response.

## API Documentation

### Endpoints

- `GET /`: Welcome message
- `POST /api/query`: Query the LLAMA 3.1 model

### Request Format

```json
{
  "question": "Your question here"
}
```

### Response Format

```json
{
  "response": "<div class=\"llama-response\"><p>HTML-formatted answer here</p></div>"
}
```

## Development

### Running Tests

```
pytest tests/
```

### Adding New Features

1. Implement new functionality in the appropriate module.
2. Add corresponding tests in the `tests/` directory.
3. Update this README if necessary.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Meta for the LLAMA 3.1 model
- Ollama for providing easy model deployment
- FastAPI for the web framework

