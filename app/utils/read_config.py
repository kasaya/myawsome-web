# -*- coding: utf-8 -*-
# read_config.py
# @Author ouyang
# @Description  
# @Created  2022-01-10T15:38:06.764Z+08:00
# @Modified  2022-01-10T15:38:06.764Z+08:00
#
import yaml
from app.utils.common import singleton


@singleton
class ReadConfig(object):
    __data:dict
    def __init__(self) -> None:
       with open('./config/config.yml', 'r') as file:
           self.__data = yaml.load(file.read(), Loader=yaml.FullLoader)

    #读取配置文件
    def get_config(self, name:str):
        assert name != None and name != ''
        names:list = name.split('.')
        obj = self.__data[names[0]]
        for key in names[1:]:
            obj = obj[key]
        return obj

if __name__== '__main__':
    rc = ReadConfig()
    print(rc.get_config('sql.url'))