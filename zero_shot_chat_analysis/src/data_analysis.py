from __future__ import annotations

import json
import os


def load_dialog(filename):
    print(f"Loading dialog... {filename}")
    with open(os.path.join("zero_shot_chat_analysis/data/input", filename + ".json")) as file:
        return json.load(file)
