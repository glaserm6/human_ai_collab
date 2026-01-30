def extract_three_words(text):
    words = text.strip().split()
    return " ".join(words[:3])

def format_nudge(text):
    lines = text.split("\n")
    question = ""
    sparks = ""

    for line in lines:
        if "Question" in line:
            question = line.split(":", 1)[-1].strip()
        if "Sparks" in line:
            sparks = line.split(":", 1)[-1].strip()

    return question, sparks
