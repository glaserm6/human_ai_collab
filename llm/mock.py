from .base import LLMClient
import random

class MockLLM(LLMClient):
    def complete(self, prompt: str) -> str:
        mock_responses = [
            "in the margin",
            "as a result",
            "which suggests that"
        ]
        return random.choice(mock_responses)
