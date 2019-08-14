"""
------------------------------------
@Time : 2019/8/13 20:33
@Auth : linux超
@File : log.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import os
import logging
from logging.handlers import RotatingFileHandler

from common.dirAndTime import DirTime as Dt
from config.globalconf import LOG_DIR as LOG_DIR


class Log(object):
    """记录日志"""
    def __init__(self, name=__name__, path='log.log', level='DEBUG'):
        self._name = name
        self._path = path
        self._level = level
        self._logger = logging.getLogger(self._name)
        self._logger.setLevel(self._level)

    def _init_handler(self):
        file_handler = RotatingFileHandler(self._path,
                                           maxBytes=10 * 1024 * 1024,
                                           backupCount=3,
                                           encoding='utf-8')
        return file_handler

    def _set_handler(self, file_handler, level='DEBUG'):
        file_handler.setLevel(level)
        return self._logger.addHandler(file_handler)

    @staticmethod
    def _set_formatter(file_handler):
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]'
                                      '-%(levelname)s-[日志信息]: %(message)s',
                                      datefmt='%a, %d %b %Y %H:%M:%S')
        return file_handler.setFormatter(formatter)

    @staticmethod
    def _close_handler(file_handler):
        return file_handler.close()

    @property
    def logger(self):
        file_handler = self._init_handler()
        self._set_handler(file_handler)
        self._set_formatter(file_handler)
        self._close_handler(file_handler)
        return self._logger


log_name = Dt.file_name("log", "log")
log_path = os.path.join(LOG_DIR, log_name)
log = Log(__name__, log_path)
logger = log.logger


if __name__ == '__main__':
        logger.info("Linux超2")
