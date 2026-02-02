# ui/baseline_ui.py

import gradio as gr

def baseline_components():
    problem_box = gr.Textbox(label="Problem", interactive=False)
    ai_btn = gr.Button("Let AI Write For You")
    ai_output = gr.Textbox(label="AI Solution")
    return problem_box, ai_btn, ai_output
