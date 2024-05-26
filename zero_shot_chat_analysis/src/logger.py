from __future__ import annotations

import logging


def setup_logger(logger_name):
    """
    setup logger for keeping track of log outputs.
    Args:
        logger_name(str): logger name.
    Return:
        logger instance.
    """
    logger = logging.getLogger(logger_name)
    logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
    logger.info("Started....")

    return logger
