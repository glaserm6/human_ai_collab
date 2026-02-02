# data/logger.py

import csv
from datetime import datetime

def log_row(data):
    """
    Append a row of study data with timestamp
    """
    with open("study_data.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data + [datetime.now()])
