from loguru import logger


class FileLogger:
    def __init__(self, filename, rotation="500 MB"):
        self.filename = filename
        self.rotation = rotation
        self.logger = self._setup_logger()

    def _setup_logger(self):
        logger.add(self.filename, rotation=self.rotation)
        return logger

    def log_info(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_exception(self, message):
        self.logger.exception(message)