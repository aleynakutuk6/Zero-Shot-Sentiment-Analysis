import json
import os


def read_dialog(filename):
    print(f"Reading dialog... {filename}")
    with open(os.path.join(os.getcwd(), "data", filename + ".json")) as file:
        return json.load(file)


