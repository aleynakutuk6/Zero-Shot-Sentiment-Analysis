from __future__ import annotations

import argparse
import configparser
import os

import datasets

from tqdm import tqdm
from data import load_dataset
from utils.model_loading import get_model
from utils.logger import setup_logger


def main():
    parser = argparse.ArgumentParser(description="Sentiment and Intention Analysis of a customer.")
    parser.add_argument(
        "-cfg",
        "--config",
        type=str,
        required=True,
        metavar="FILE",
        help="path to config file.",
    )
    parser.add_argument(
        "-o",
        "--output_path",
        type=str,
        default="outputs",
        help="path to save model outputs.",
    )
    parser.add_argument(
        "-d",
        "--data_path",
        type=str,
        default=None,
        help="data path for a dialog between a customer and an agent.",
    )
    args = parser.parse_args()

    # reading config file
    assert args.config is not None
    config = configparser.ConfigParser()
    config.read(args.config)
    model_name = config.get("model", "model_name")
    intent_labels = config.get("labels", "intent_labels")
    sentiment_labels = config.get("labels", "sentiment_labels")

    logger = setup_logger("zero-shot-classification")
    logger.info("Using model name: {}".format(model_name))
    logger.info("Intent labels: {}".format(intent_labels))
    logger.info("Sentiment labels: {}".format(sentiment_labels))
    logger.info("*"*100)

    # Preparing Dataset
    # if args.data_path provided, reading json from that path;
    # otherwise reading according to config file provided.
    dataset_name = config.get("dataset", "dataset_name")
    data_path = config.get("dataset", "data_path")
    batch_size = int(config.get("dataset", "batch_size"))
    if args.data_path is not None:
        data_path = args.data_path
    dataset = load_dataset(dataset_name, data_path)

    # Model Loading
    model = get_model(model_name, logger)

    if args.output_path is not None:
        os.system(f"mkdir -p {args.output_path}")

    # Sentiment and Intention Analysis
    logger.info("Sentiment analysis started...")
    for out in tqdm(model(dataset, candidate_labels=sentiment_labels, batch_size=batch_size), total=len(dataset)):
        print("Sentiment results:", out)

    logger.info("Intention analysis started...")
    for out in tqdm(model(dataset, candidate_labels=intent_labels, batch_size=batch_size), total=len(dataset)):
        print("Intention results", out)


if __name__ == "__main__":
    main()