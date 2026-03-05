def socratic_response(question: str) -> str:
    if "square" in question.lower():
        return "What happens when you multiply a number by itself?"

    if "even" in question.lower():
        return "What operator tells you the remainder after division?"

    if "factorial" in question.lower():
        return "How could you express factorial in terms of smaller factorials?"

    return "What smaller step could you solve first?"