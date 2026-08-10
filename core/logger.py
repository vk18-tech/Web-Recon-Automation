import logging
from pathlib import Path


def setup_logger():

    log_directory = Path("logs")
    log_directory.mkdir(exist_ok=True)

    log_file = log_directory / "recon.log"

    logger = logging.getLogger("WebRecon")
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers if setup_logger() is called again
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        log_file,
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger