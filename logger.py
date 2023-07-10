import logging
import logging.handlers
import sys
import pathlib
import publisher_pb2 as pb2


class PluginLogger:

    def __init__(self, name: str = '', log_path: str = 'logs'):
        self.__log_prefix: str = ''
        self.__file_name: str = pathlib.PurePath(sys.path[1]).name + "-log.txt"
        self.__level = pb2.LogLevel.Info

        if not name:
            name = self.__file_name

        print(f'name:{name}, path:{log_path}')
        # ensure log directory exists
        pathlib.Path(log_path).mkdir(parents=True, exist_ok=True)

        # setup logger
        self.__logger = logging.getLogger(name)
        self.__logger.setLevel(logging.INFO)
        # self.__logger.propagate(False)
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s", '%Y-%m-%d %H:%M:%S %z'
        )
        handler = logging.handlers.TimedRotatingFileHandler(filename=f'{log_path}/{self.__file_name}', when='d',
                                                            interval=1, backupCount=10)
        handler.setFormatter(formatter)
        self.__logger.addHandler(handler)

    def __map_log_level(self):
        # Error = 0;
        # Warn = 1;
        # Info = 2;
        # Debug = 3;
        # Trace = 4;
        if self.__level == pb2.LogLevel.Error:
            return logging.ERROR
        elif self.__level == pb2.LogLevel.Warn:
            return logging.WARN
        elif self.__level == pb2.LogLevel.Info:
            return logging.INFO
        elif self.__level == pb2.LogLevel.Debug:
            return logging.DEBUG
        else:
            return logging.NOTSET

    def debug(self, message: str):
        print(f'level:{self.__level}, enum:{logging.DEBUG}')
        # if self.__level < logging.DEBUG:
        #     return
        self.__logger.debug(f'{self.__log_prefix} {message}')

    def info(self, message: str):
        # if self.__level < logging.INFO:
        #     return
        self.__logger.info(f'{self.__log_prefix} {message}')

    def error(self, message: str):
        # if self.__level < logging.ERROR:
        #     return
        self.__logger.error(f'{self.__log_prefix} {message}')

    def set_log_level(self, level):
        self.__level = level
        self.__logger.setLevel(self.__map_log_level())

    def set_log_prefix(self, log_prefix: str):
        self.__log_prefix = log_prefix


if __name__ == '__main__':
    logger = PluginLogger(name='test')
    logger.set_log_prefix('test pref001')
    from datetime import datetime
    logger.debug(f'{datetime.now()} - this is a debug message')
    logger.info(f'{datetime.now()} - this is a info message')
    logger.error(f'{datetime.now()} - this is a error message')
    # logger.debug(f'{datetime.now()} - this is a debug message')

    logger.set_log_level(pb2.LogLevel.Debug)
    logger.debug(f'{datetime.now()} - this is 2nd debug message')
    logger.info(f'{datetime.now()} - this is 2nd info message')
    logger.error(f'{datetime.now()} - this is 2nd error message')
