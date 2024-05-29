from transformers import pipeline

import os


def get_model(model_name, logger):

    model_path = os.path.join("resources", model_name)
    # if there is .bin file in resources/<model_name> directory, load from .bin directly
    if os.path.exists(os.path.join(model_path)):
        logger.info("Loading the model from local {}...".format(model_path))
        model = pipeline("zero-shot-classification", model_path, batch_size=30)

    # loading from hugging face transformers library
    else:
        logger.info("Downloading the model from hugging face...")
        model = pipeline("zero-shot-classification", 'facebook/bart-large-mnli')
        model.save_pretrained(model_path)

    return model
