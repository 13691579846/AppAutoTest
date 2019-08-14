"""
------------------------------------
@Time : 2019/8/8 10:37
@Auth : linux超
@File : dirAndTime.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from datetime import datetime
import os


class DirTime(object):
    @staticmethod
    def current_date() -> str:
        return datetime.strftime(datetime.today(), '%Y_%m_%d')

    @staticmethod
    def current_time() -> str:
        return datetime.now().strftime('%H_%M_%S')

    @staticmethod
    def file_name(file_type: str, context='') -> str:
        """
        文件名
        :param file_type:  文件后缀
        :param context: 说明性文本拼接到文件名中
        :return: file name
        """
        if file_type.lower() == "log":
            name = DirTime.current_date() + context + ".log"
        else:
            name = DirTime.current_date() + '_' + DirTime.current_time() + context + '.' + file_type
        return name

    @staticmethod
    def create_path(path):
        if not os.path.exists(path):
            os.makedirs(path)
        return path


if __name__ == '__main__':
    pass
