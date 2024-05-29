from __future__ import annotations

import argparse
import configparser

from data_analysis import read_dialog
from model_loading import get_model
from logger import setup_logger


def main():
    parser = argparse.ArgumentParser(description="Sentiment and Intention Analysis of a customer.")
    parser.add_argument(
        "-d",
        "--dialog",
        type=str,
        required=True,
        help="The filename of the dialog data. The data should be kept in JSON format.",
    )
    parser.add_argument(
        "-cfg",
        "--config",
        type=str,
        default="",
        metavar="FILE",
        help="path to config file.",
    )
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.config)
    model_name = config.get("model", "model_name")

    logger = setup_logger("zero-shot-classification")
    logger.info("Using {} Model".format(model_name))
    logger.info("Intent labels: {}".format(config.get("labels", "intent_labels")))
    logger.info("Sentiment labels: {}".format(config.get("labels", "sentiment_labels")))

    print(read_dialog(args.dialog))
    get_model(model_name, logger)


if __name__ == "__main__":
    main()
