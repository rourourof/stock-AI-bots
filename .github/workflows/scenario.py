import json
import os

FILE = "scenario_prev.json"

def save_scenario(text):
    with open(FILE, "w") as f:
        json.dump({"text": text}, f)

def load_prev_scenario():
    if not os.path.exists(FILE):
        return None
    with open(FILE) as f:
        return json.load(f)["text"]
