import gradio as gr
from logic.condition_manager import get_tasks
from llm.mock import MockModel
from core.prompts import BASELINE_PROMPT, NUDGE_PROMPT
from core.constraints import NUDGE_CONSTRAINT
from data.logger import log_row
from logic.evaluator import evaluate_code

model = MockModel()

user_level = ""
baseline_task = ""
nudge_task = ""

# ---------------- FUNCTIONS ---------------- #

def start_study(level):
    global user_level, baseline_task, nudge_task
    user_level = level
    baseline_task, nudge_task = get_tasks(level)
    return baseline_task, gr.update(visible=True)

def run_baseline():
    return model.generate(BASELINE_PROMPT + baseline_task)

def provide_nudge(code):
    prompt = NUDGE_PROMPT + "\nProblem:\n" + nudge_task + "\n" + NUDGE_CONSTRAINT
    return model.generate(prompt)

def check_code(code):
    return "Correct!" if evaluate_code(code) else "Not quite — try again or use Nudge."

def finish_survey(*answers):
    log_row([user_level] + list(answers))
    return "🎉 Study complete. Thank you!"

# ---------------- UI ---------------- #

with gr.Blocks() as demo:

    gr.Markdown("# 🤖 Human-AI Collaborative Learning Study")
    gr.Markdown("### Exploring how AI affects confidence, ownership, and problem solving")

    # ---------- PRE-SURVEY ----------
    gr.Markdown("---")
    gr.Markdown("## Step 1: Your Experience Level")

    level = gr.Radio(["Beginner","Intermediate","Advanced"],
                     label="How comfortable are you with Python?")
    start_btn = gr.Button("Start Study 🚀")

    baseline_problem = gr.Textbox(label="Problem", interactive=False)

    # ---------- MAIN SECTION ----------
    main_section = gr.Column(visible=False)

    with main_section:

        gr.Markdown("---")
        gr.Markdown("## 🧩 Part 1 — AI Solves the Problem (Baseline)")
        ai_btn = gr.Button("Let AI Write the Solution")
        ai_solution = gr.Code(label="AI Solution", language="python")

        gr.Markdown("---")
        gr.Markdown("## ✍️ Part 2 — You Solve with AI Nudges")
        code_box = gr.Code(label="Write Your Code Here", language="python")
        nudge_btn = gr.Button("💡 Nudge Me")
        nudge_output = gr.Textbox(label="AI Nudge")
        check_btn = gr.Button("Check My Code")
        result = gr.Textbox(label="Result")

        # ---------- SURVEY ----------
        gr.Markdown("---")
        gr.Markdown("## 📋 Final Survey")
        gr.Markdown("Select the option that best matches how you felt.")

        LIKERT = [
            "1",
            "2",
            "3",
            "4",
            "5"
        ]

        gr.Markdown("""
        ### How to Answer
        Rate your confidence for each statement:

        | Score | Meaning |
        |------|---------|
        | **1** | Not confident at all |
        | **2** | Slightly confident |
        | **3** | Neutral |
        | **4** | Somewhat confident |
        | **5** | Very confident |
        """)

        gr.Markdown("### Baseline (AI wrote the solution)")

        b1 = gr.Radio(LIKERT, label="I felt confident understanding the AI solution")
        b2 = gr.Radio(LIKERT, label="I felt in control of the outcome")
        b3 = gr.Radio(LIKERT, label="The solution felt like it belonged to me")
        b4 = gr.Radio(LIKERT, label="I could explain how the solution works")
        b5 = gr.Radio(LIKERT, label="I felt engaged during this phase")

        gr.Markdown("### Nudge Phase (I wrote code with AI help)")
        n1 = gr.Radio(LIKERT, label="I felt confident solving the problem")
        n2 = gr.Radio(LIKERT, label="I felt ownership over my solution")
        n3 = gr.Radio(LIKERT, label="The nudges helped without giving the answer")
        n4 = gr.Radio(LIKERT, label="I understood my solution deeply")
        n5 = gr.Radio(LIKERT, label="I felt actively involved in problem-solving")

        submit_btn = gr.Button("Submit Survey")
        thanks = gr.Textbox()



    # ---------- ACTIONS ----------
    start_btn.click(start_study, inputs=level, outputs=[baseline_problem, main_section])
    ai_btn.click(run_baseline, outputs=ai_solution)
    nudge_btn.click(provide_nudge, inputs=code_box, outputs=nudge_output)
    check_btn.click(check_code, inputs=code_box, outputs=result)
    submit_btn.click(
        finish_survey,
        inputs=[b1,b2,b3,b4,b5,n1,n2,n3,n4,n5],
        outputs=thanks
    )

demo.launch(theme=gr.themes.Soft())
