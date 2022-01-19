# -*- coding: utf-8 -*-
# customer_exception.py
# @Author ouyang
# @Description  
# @Created  2022-01-13T15:08:12.074Z+08:00
# @Modified  2022-01-13T15:08:12.074Z+08:00
#
from dataclasses import dataclass



@dataclass()
class AppcationExcetpion(Exception):
    err_code:str
    name: str
    err_message:str

    
