import requests
from .base import LLMClient

class HuggingFaceLLM(LLMClient):
    def __init__(self, api_key, model="gpt2"):
        self.api_key = api_key
        self.model = model

    def complete(self, prompt: str) -> str:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {"inputs": prompt}

        response = requests.post(
            f"https://api-inference.huggingface.co/models/{self.model}",
            headers=headers,
            json=payload
        )

        return response.json()[0]["generated_text"]
