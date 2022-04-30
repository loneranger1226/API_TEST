import logging, time, os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

LOG_PATH = os.path.join(BASE_PATH, "log")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class Logger(object):
    def __init__(self):
        self.log_name = os.path.join(LOG_PATH, f"{time.strftime('%Y%m%d')}.log")
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)

        self.formatter = logging.Formatter("[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s")

        self.file_logger = logging.FileHandler(self.log_name, mode='a', encoding='utf-8')
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        self.file_logger.setLevel(logging.DEBUG)
        self.console.setFormatter(self.formatter)
        self.logger.addHandler(self.file_logger)
        self.logger.addHandler(self.console)

logger = Logger().logger

if __name__ == '__main__':
    logger.info("-----测试开始-----")
    logger.debug("-----测试结束-----")