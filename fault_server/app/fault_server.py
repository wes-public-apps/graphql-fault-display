from sys import stdout
import logging
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(stdout))
logger.addHandler(logging.FileHandler("server.log", mode='a', encoding='utf-8'))
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    logging.info("Hello server!!!!")
