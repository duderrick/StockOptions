import logging


def setup_logging(logger_name: str, logging_level: int) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging_level)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)
    return logger
