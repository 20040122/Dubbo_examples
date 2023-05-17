# 封装基础服务类
from dubboclient import DubboClient


class BaseService(object):
    def __init__(self):
        self.dubboclt = DubboClient("211.103.136.244",6502)