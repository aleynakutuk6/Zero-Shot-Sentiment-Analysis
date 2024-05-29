from torch.utils.data import Dataset

import json
import os


class DialogDataset(Dataset):
    def __init__(self, filepath):
        with open(filepath) as file:
            data = json.load(file)

        self.messages = [d["message"] for d in data]

    def __len__(self):
        return len(self.messages)

    def __getitem__(self, index):
        return self.messages[index]
