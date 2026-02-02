# llm/base.py

class BaseModel:
    """
    Base class for all LLM models.
    Defines the interface for generate().
    """
    def generate(self, prompt):
        """
        Generate a response given a prompt.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement generate()")
