import logging


def setup_logger(logger_name):
    # setup logger for keeping track of log outputs.

    logger = logging.getLogger(logger_name)
    logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
    logger.info("*" * 100)
    logger.info("Started...")

    return logger
