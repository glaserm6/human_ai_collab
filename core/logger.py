import time

def log_event(event: str):
    timestamp = time.time()
    print(f"{timestamp}: {event}")