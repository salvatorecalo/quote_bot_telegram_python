import logging
import sys

def setup_logger(name: str, level=logging.INFO) -> logging.Logger:
    """
    Configure logger to show message in console
    Args: 
        name (str): name of the logger
        level: logging level, default is logging.INFO
    Returns:
        logging.Logger: configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if logger.hasHandlers():
        return logger
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.propagate = False
    return logger