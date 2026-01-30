def next_three_words_prompt(text):
    return f"""
You are a writing assistant.
Given the text below, suggest exactly THREE next words.
Do not explain.
Do not complete the sentence.

TEXT:
{text}

THREE WORDS:
"""

def metacognitive_prompt(text):
    return f"""
You are a writing coach.
Do NOT write content.

1. Ask ONE reflective question about the writing.
2. Provide 3–5 ONE-WORD sparks.

TEXT:
{text}

FORMAT:
Question:
Sparks:
"""
