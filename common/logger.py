import logging
import os

_LOGGER_CONFIGURED = False

def setup_logging():
    global _LOGGER_CONFIGURED
    if _LOGGER_CONFIGURED:
        return

    level = os.getenv("LOG_LEVEL", "INFO").upper()

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    _LOGGER_CONFIGURED = True


def get_logger(name: str) -> logging.Logger:
    setup_logging()
    return logging.getLogger(name)
