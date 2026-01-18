import json
import os
from datetime import datetime

RESULTS_DIR = "data/results"

def save_attempt(report):
    os.makedirs(RESULTS_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
    filename = f"title-{report['title']}__time-{timestamp}__{report['summary']['percentage']}pct.json"

    path = os.path.join(RESULTS_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

    return path

