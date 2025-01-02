import json
import os

def save_game_state(filename: str, data: dict):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def load_game_state(filename: str) -> dict:
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return {}