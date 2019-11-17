"""
------------------------------------
@Time : 2019/8/10 22:06
@Auth : linux超
@File : parseYaml.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from config.globalconf import YML_PATH
import yaml


class ParseYml(object):

    def __init__(self, file):
        self.file = file

    @property
    def read_alone(self):
        with open(self.file, 'r', encoding='utf8') as f:
            context = yaml.load(f, Loader=yaml.FullLoader)
        return context

    @property
    def read_all(self):
        with open(self.file, 'r', encoding='utf8') as f:
            contexts = yaml.load_all(f, Loader=yaml.FullLoader)
        return contexts

    def write_alone(self, context):
        with open(self.file, 'w', encoding='utf8') as f:
            return yaml.dump(context, f)

    def write_all(self, *context):
        with open(self.file, 'w', encoding='utf8') as f:
            return yaml.dump_all(list(context), f)


if __name__ == '__main__':
    yml = ParseYml(YML_PATH)
    con = yml.read_alone
    print(con)
