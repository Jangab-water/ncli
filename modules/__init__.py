import logging
import logging.handlers
import os


class BaseModule:
    def __init__(self, name: str, log_level: str, expose_dnager: bool=False):
        self.name=name
        self.logger=self.__build_logger(self.name, level=log_level)
        
    def __create_logpath(self, name: str):
        try:
            os.mkdir(name)
        except FileExistsError as e:
            return 1
        except Exception as e:
            return -1
        return 0
            
    def __build_logger(self, name: str, level: str):
        logger=logging.getLogger(name)
        logger.setLevel(level)
        hdlr=logging.handlers.TimedRotatingFileHandler(filename=f"./logs/{self.name}.log", when='D', utc=True, interval=1, backupCount=10)
        formatter=logging.Formatter(
            "%(asctime)s - %(levelname)s :: [%(name)s - %(filename)s:%(lineno)d] - %(message)s"
        )
        
        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr)
        return logger