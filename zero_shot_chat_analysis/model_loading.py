from transformers import pipeline

import os


def get_model(model_name, logger):

    model_path = os.path.join(os.getcwd(), "resources", model_name)
    if os.path.exists(os.path.join(model_path, "pytorch_model.bin")):
        logger.info("Loading the model...")
        classifier = pipeline("zero-shot-classification", model_path)
    else:
        classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        classifier.save_pretrained(model_path)

    return classifier
