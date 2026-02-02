# logic/evaluator.py

import io
import sys

def evaluate_code(code, expected_output=None):
    """
    Evaluate Python code. If expected_output is provided, compare.
    Otherwise, just check if code runs without errors.
    """
    buffer = io.StringIO()
    sys.stdout = buffer
    try:
        exec(code)
        output = buffer.getvalue().strip()
        sys.stdout = sys.__stdout__
        if expected_output is not None:
            return output == expected_output
        return True
    except Exception as e:
        sys.stdout = sys.__stdout__
        return False
