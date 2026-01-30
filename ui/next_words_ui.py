import gradio as gr
from core.prompts import next_three_words_prompt
from core.constraints import extract_three_words

def build_next_words_ui(llm):
    with gr.Column():
        gr.Markdown("### ✍️ Co-Pilot: Next 3 Words")

        text_input = gr.Textbox(
            lines=12,
            label="Your Writing",
            placeholder="Start writing..."
        )

        btn = gr.Button("Suggest Next 3 Words")

        output = gr.Textbox(
            label="AI Suggestion",
            interactive=False
        )

        def run(text):
            prompt = next_three_words_prompt(text)
            raw = llm.complete(prompt)
            return extract_three_words(raw)

        btn.click(run, text_input, output)
