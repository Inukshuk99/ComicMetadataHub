"""
ComicMetadataHub Logging System
"""

import logging
import os

from .config import LOG_DIR


def setup_logger(name="ComicMetadataHub"):
    """
    Creates and returns the application logger.
    """

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    log_file = os.path.join(
        LOG_DIR,
        "ComicMetadataHub.log"
    )

    file_handler = logging.FileHandler(
        log_file,
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


logger = setup_logger()