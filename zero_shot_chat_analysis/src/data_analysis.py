import json
import os


def read_dialog(filename):
    print(f"Reading dialog... {filename}")
    with open(os.path.join(os.getcwd(), "zero_shot_chat_analysis/data/input", filename + ".json")) as file:
        return json.load(file)


