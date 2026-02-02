# logic/condition_manager.py

from core.python_tasks import tasks

def get_tasks(level):
    """
    Return the baseline and nudge task for the given level
    """
    if level not in tasks:
        raise ValueError(f"Unknown level: {level}")
    return tasks[level]["baseline"], tasks[level]["nudge"]
