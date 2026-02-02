# llm/mock.py

from .base import BaseModel  # relative import

class MockModel(BaseModel):
    def generate(self, prompt):
        if "Problem:" in prompt:
            return "print('This is a mock solution')"
        return "Mock nudge: Think about loops."
