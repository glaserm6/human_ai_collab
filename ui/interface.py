import gradio as gr

from core.levels import LEVEL_DESCRIPTIONS
from core.phases import PHASE_QUESTIONS
from core.validator import validate_code
from ai.three_word import generate_three_word_hint
from ai.socratic import socratic_response


def launch_interface():

    CUSTOM_CSS = """
    .survey-button {
        background: linear-gradient(90deg, #6a11cb, #2575fc);
        color: white !important;
        font-size: 20px !important;
        padding: 18px 28px !important;
        border-radius: 14px !important;
        border: none;
    }
    """

    # -------------------------
    # LOGIC FUNCTIONS
    # -------------------------

    def select_level():
        return (
            gr.update(visible=False),
            gr.update(value=PHASE_QUESTIONS[1], visible=True),
            gr.update(visible=True),
            gr.update(visible=True),
            1
        )

    def check_code(user_code, phase):

        if validate_code(user_code, phase):

            if phase == 1:
                return (
                    gr.update(value="✅ Correct! Welcome to Phase 2.", visible=True),
                    PHASE_QUESTIONS[2],
                    gr.update(visible=True),
                    gr.update(visible=False),
                    2,
                    gr.update(visible=False)
                )

            elif phase == 2:
                return (
                    gr.update(value="✅ Correct! Welcome to Phase 3.", visible=True),
                    PHASE_QUESTIONS[3],
                    gr.update(visible=False),
                    gr.update(visible=True),
                    3,
                    gr.update(visible=False)
                )

            else:
                return (
                    gr.update(value="🎉 Excellent work! Simulation complete.", visible=True),
                    "",
                    gr.update(visible=False),
                    gr.update(visible=False),
                    3,
                    gr.update(visible=True)
                )

        else:
            return (
                gr.update(value="❌ Incorrect. Try again.", visible=True),
                PHASE_QUESTIONS[phase],
                gr.update(),
                gr.update(),
                phase,
                gr.update()
            )

    def three_word_hint(phase):
        return gr.update(
            value=generate_three_word_hint(PHASE_QUESTIONS[phase]),
            visible=True
        )

    def socratic_help(phase):
        return gr.update(
            value=socratic_response(PHASE_QUESTIONS[phase]),
            visible=True
        )

    # -------------------------
    # UI
    # -------------------------

    with gr.Blocks() as demo:

        phase_state = gr.State(1)

        gr.Markdown("# 🧠 Human–AI Collaborative Coding Study")

        # COMPONENTS (defined first)

        level_section = gr.Column()

        question_box = gr.Textbox(
            label="Python Question",
            visible=False
        )

        code_box = gr.Code(
            language="python",
            label="Your Code",
            lines=12,
            visible=False,
            interactive=True
        )

        check_btn = gr.Button(
            "Check Code",
            visible=False
        )

        feedback = gr.Textbox(
            label="Feedback",
            visible=False
        )

        three_word_btn = gr.Button(
            "3 Word Hint",
            visible=False
        )

        socratic_btn = gr.Button(
            "Socratic AI Help",
            visible=False
        )

        survey_btn = gr.HTML(
            """
            <a href="https://nku.co1.qualtrics.com/jfe6/preview/previewId/8b95e814-8d67-4e73-85d4-ce55dc2fd8a2/SV_5itu7fMR9GqAREi?Q_CHL=preview&Q_SurveyVersionID=current" target="_blank">
                <button class="survey-button">
                    Continue to Post-Study Survey
                </button>
            </a>
            """,
            visible=False
        )

        # -------------------------
        # EXPERIENCE LEVEL
        # -------------------------

        with level_section:

            gr.Markdown("## Select Your Python Experience Level")

            for level, desc in LEVEL_DESCRIPTIONS.items():

                with gr.Row():

                    level_btn = gr.Button(level)

                    gr.Markdown(f"*{desc}*")

                    level_btn.click(
                        select_level,
                        outputs=[
                            level_section,
                            question_box,
                            code_box,
                            check_btn,
                            phase_state
                        ]
                    )

        # -------------------------
        # BUTTON CONNECTIONS
        # -------------------------

        check_btn.click(
            check_code,
            inputs=[code_box, phase_state],
            outputs=[
                feedback,
                question_box,
                three_word_btn,
                socratic_btn,
                phase_state,
                survey_btn
            ]
        )

        three_word_btn.click(
            three_word_hint,
            inputs=phase_state,
            outputs=feedback
        )

        socratic_btn.click(
            socratic_help,
            inputs=phase_state,
            outputs=feedback
        )

    return demo, CUSTOM_CSS