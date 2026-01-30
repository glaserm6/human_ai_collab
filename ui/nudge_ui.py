import gradio as gr
from core.prompts import metacognitive_prompt
from core.constraints import format_nudge

def build_nudge_ui(llm):
    with gr.Column():
        gr.Markdown("### 🧠 Reflective Writing Nudge")

        text_input = gr.Textbox(lines=12, label="Your Writing")

        btn = gr.Button("Get Nudge")

        question = gr.Textbox(label="Reflective Question")
        sparks = gr.Textbox(label="One-Word Sparks")

        def run(text):
            raw = llm.complete(metacognitive_prompt(text))
            return format_nudge(raw)

        btn.click(run, text_input, [question, sparks])
