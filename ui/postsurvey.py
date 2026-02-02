# ui/postsurvey_ui.py

import gradio as gr

def postsurvey_components():
    agency = gr.Slider(1,5,label="I felt in control of the solution")
    ownership = gr.Slider(1,5,label="The solution feels like mine")
    confidence = gr.Slider(1,5,label="I understand the solution")
    submit_btn = gr.Button("Submit Survey")
    thanks = gr.Textbox()
    return agency, ownership, confidence, submit_btn, thanks
