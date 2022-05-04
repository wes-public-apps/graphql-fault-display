from logging import *
from sys import stdout


def enable_logging(app_name: str) -> None:
    logger = getLogger()
    logger.addHandler(StreamHandler(stdout))
    logger.addHandler(FileHandler(f"{app_name}.log", mode='a', encoding='utf-8'))
    logger.setLevel(DEBUG)
    info(f'{app_name}: logging enabled')
