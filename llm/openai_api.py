# llm/openai_api.py

# Use relative import
from .base import BaseModel
import openai

class OpenAIModel(BaseModel):
    """
    Connect to OpenAI API to generate Python solutions or nudges.
    Replace 'YOUR_API_KEY' with your actual key when funded.
    """
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )
        return response.choices[0].message.content
