from __future__ import annotations

import argparse
import configparser

from data_analysis import load_dialog
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

    logger = setup_logger("zeroshotchatanalysis")
    logger.info("Using {} Model".format(config.get("model", "model_name")))
    logger.info("Intent labels: {}".format(config.get("labels", "intent_labels")))
    logger.info("Sentiment labels: {}".format(config.get("labels", "sentiment_labels")))

    print(load_dialog(args.dialog))


if __name__ == "__main__":
    main()
