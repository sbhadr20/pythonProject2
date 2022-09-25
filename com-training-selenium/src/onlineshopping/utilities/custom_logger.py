import logging
import os


class CustomLog:

    @staticmethod
    def log():
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", ".."))
        log_path = os.path.join(root_dir, 'Logs', 'test.log')
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler(log_path)
        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%d-%m-%Y %I:%M:%S %p')
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)
        logger.info("*** Logger setup successful***")
        return logger
