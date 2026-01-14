import json
import os

FILE = "scenario_prev.json"

def save_scenario(text):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump({"scenario": text}, f, ensure_ascii=False)

def load_prev_scenario():
    if not os.path.exists(FILE):
        return None
    with open(FILE, encoding="utf-8") as f:
        return json.load(f)["scenario"]
