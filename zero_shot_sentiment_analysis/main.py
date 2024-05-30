import argparse
import configparser
import os
import sys

sys.path.append(os.getcwd())

from tqdm import tqdm
from zero_shot_sentiment_analysis.data import load_dataset
from zero_shot_sentiment_analysis.utils.io_utils import write_sentiment_intent_results
from zero_shot_sentiment_analysis.utils.logger import setup_logger
from zero_shot_sentiment_analysis.utils.model_loading import get_model


def main():
    parser = argparse.ArgumentParser(description="Sentiment and Intention Analysis")
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

    logger = setup_logger("zero-shot-sentiment-analysis")
    logger.info(f"Using model name: {model_name}")
    logger.info(f"Intent labels: {intent_labels}")
    logger.info(f"Sentiment labels: {sentiment_labels}")
    logger.info("*" * 100)

    # Preparing Dataset
    # if args.data_path provided, reading json from that path;
    # otherwise reading according to config file provided.
    dataset_name = config.get("dataset", "dataset_name")
    data_path = config.get("dataset", "data_path")
    batch_size = int(config.get("dataset", "batch_size"))
    if args.data_path is not None:
        data_path = args.data_path
    if "\\" in data_path:
        filename = data_path.split("\\")[-1]
    else:
        filename = data_path.split("/")[-1]
    logger.info("Reading from data file {}...".format(filename))
    dataset = load_dataset(dataset_name, data_path)

    # Model Loading
    model = get_model(model_name, logger)

    if args.output_path is not None and not os.path.exists(args.output_path):
        os.mkdir(args.output_path)

    # Sentiment and Intention Analysis
    results = []
    logger.info("Sentiment and intention analysis started...")
    for sent_out, intent_out in tqdm(
        zip(
            model(dataset, candidate_labels=sentiment_labels, batch_size=batch_size),
            model(dataset, candidate_labels=intent_labels, batch_size=batch_size),
        ),
        total=len(dataset),
    ):
        results.append([sent_out, intent_out])

    # Model outputs are saved.
    save_path = os.path.join(args.output_path, "out_" + filename)
    write_sentiment_intent_results(results, save_path)
    logger.info(f"Output is saved to path: {save_path}")
    logger.info("DONE!!!!")


if __name__ == "__main__":
    main()
