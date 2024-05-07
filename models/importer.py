from os import path, curdir
from logging import getLogger
from logging.config import fileConfig


ROOT_DIR = path.abspath(curdir)


def get_logger_object() -> object:
    fileConfig('configs\\logging.ini', disable_existing_loggers=False)
    logger = getLogger(__name__)
    return logger


logger = get_logger_object()


