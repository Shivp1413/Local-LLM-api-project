# src/model/llama_wrapper.py

import ollama

class LlamaWrapper:
    def __init__(self):
        self.model = "llama:3.1"

    def generate(self, prompt):
        response = ollama.generate(model=self.model, prompt=prompt)
        return response['response']
