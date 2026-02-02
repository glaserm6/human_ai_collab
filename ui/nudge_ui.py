# ui/nudge_ui.py

import gradio as gr

def nudge_components():
    code_box = gr.Code(label="Write Your Code")
    nudge_btn = gr.Button("Nudge Me")
    nudge_output = gr.Textbox(label="Nudge")
    check_btn = gr.Button("Check Code")
    result = gr.Textbox(label="Result")
    return code_box, nudge_btn, nudge_output, check_btn, result
