import gradio as gr
from llm.mock import MockLLM
# from llm.hf_api import HuggingFaceLLM

from ui.next_words_ui import build_next_words_ui
from ui.nudge_ui import build_nudge_ui

llm = MockLLM()
# llm = HuggingFaceLLM(api_key="YOUR_KEY")

with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown("# Human-AI Collaborative Writing")

    with gr.Tabs():
        with gr.Tab("Next 3 Words"):
            build_next_words_ui(llm)

        with gr.Tab("Reflective Nudge"):
            build_nudge_ui(llm)

app.launch()
