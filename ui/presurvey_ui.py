import gradio as gr

def presurvey_components():
    level = gr.Radio(["Beginner", "Intermediate", "Advanced"], label="Comfort with Python")
    start_btn = gr.Button("Start Study")
    return level, start_btn
