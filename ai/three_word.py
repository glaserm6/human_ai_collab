def generate_three_word_hint(question: str) -> str:
    # You can later replace with real AI call
    hints = {
        "square": "multiply number itself",
        "even": "use modulo operator",
        "factorial": "recursive multiplication pattern"
    }

    for key in hints:
        if key in question.lower():
            return hints[key]

    return "think step carefully"