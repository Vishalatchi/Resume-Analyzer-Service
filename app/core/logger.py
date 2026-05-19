import logging
from logging.handlers import RotatingFileHandler


def setup_logger():

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = RotatingFileHandler(
        "app.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=5
    )

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)