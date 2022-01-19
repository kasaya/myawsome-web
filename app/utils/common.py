# -*- coding: utf-8 -*-
# common.py
# @Author ouyang
# @Description  
# @Created  2022-01-15T15:03:29.263Z+08:00
# @Modified  2022-01-15T15:03:29.263Z+08:00
#

#单例注解
def singleton(cls, *args, **kwargs):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton