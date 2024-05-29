from .dialog_dataset import DialogDataset


def load_dataset(dataset_name, *args, **kwargs):
    if dataset_name == "DialogDataset":
        return DialogDataset(*args, **kwargs)
    else:
        raise ValueError("There is no dataset with this name: {}".format(dataset_name))
