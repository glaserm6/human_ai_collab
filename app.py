import gradio as gr
from logic.condition_manager import get_tasks
from llm.mock import MockModel  # Swap with OpenAIModel when funded
from core.prompts import BASELINE_PROMPT, NUDGE_PROMPT
from core.constraints import NUDGE_CONSTRAINT, BASELINE_CONSTRAINT
from data.logger import log_row
from logic.evaluator import evaluate_code

model = MockModel()  # For now, no API key

# GLOBALS
user_level = ""
baseline_task = ""
nudge_task = ""

# --- FUNCTIONS ---
def start_study(level):
    global user_level, baseline_task, nudge_task
    user_level = level
    baseline_task, nudge_task = get_tasks(level)
    return baseline_task, gr.update(visible=True)

def run_baseline():
    prompt = BASELINE_PROMPT + baseline_task
    return model.generate(prompt)

def provide_nudge(student_code):
    prompt = NUDGE_PROMPT + "\nProblem:\n" + nudge_task + "\n" + NUDGE_CONSTRAINT
    return model.generate(prompt)

def check_code(code):
    correct = evaluate_code(code)
    return "Correct!" if correct else "Not quite — try again or use Nudge."

def finish_survey(a, o, c):
    log_row([user_level, a, o, c])
    return "Study complete. Thank you!"

# --- GRADIO LAYOUT ---
with gr.Blocks() as demo:
    gr.Markdown("# Human-AI Collaborative Learning Study")

    # Pre-survey
    level = gr.Radio(["Beginner","Intermediate","Advanced"], label="Comfort with Python")
    start_btn = gr.Button("Start Study")
    baseline_problem = gr.Textbox(label="Problem", interactive=False)

    # Baseline + Nudge + Post-survey Section (hidden until start)
    main_section = gr.Column(visible=False)
    with main_section:
        # Baseline AI
        gr.Markdown("## Baseline: AI Solves the Problem")
        ai_btn = gr.Button("Let AI Write For You")
        ai_solution = gr.Textbox(label="AI Solution")

        # Student coding + nudge
        gr.Markdown("## Student Coding + Nudge")
        code_box = gr.Code(label="Write Your Code")
        nudge_btn = gr.Button("Nudge Me")
        nudge_output = gr.Textbox(label="Nudge")
        check_btn = gr.Button("Check Code")
        result = gr.Textbox(label="Result")

        # Post-survey
        gr.Markdown("## Post-Survey")
        agency = gr.Slider(1,5,label="I felt in control of the solution")
        ownership = gr.Slider(1,5,label="The solution feels like mine")
        confidence = gr.Slider(1,5,label="I understand the solution")
        submit_btn = gr.Button("Submit")
        thanks = gr.Textbox()

    # --- BUTTON ACTIONS ---
    start_btn.click(start_study, inputs=level, outputs=[baseline_problem, main_section])
    ai_btn.click(run_baseline, outputs=ai_solution)
    nudge_btn.click(provide_nudge, inputs=code_box, outputs=nudge_output)
    check_btn.click(check_code, inputs=code_box, outputs=result)
    submit_btn.click(finish_survey, inputs=[agency, ownership, confidence], outputs=thanks)

demo.launch()
