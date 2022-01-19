# -*- coding: utf-8 -*-
# login_schemas.py
# @Author ouyang
# @Description  
# @Created  2022-01-13T10:49:19.275Z+08:00
# @Modified  2022-01-13T10:49:19.275Z+08:00
#

from pydantic import BaseModel, Field
from typing import Optional

class LoginBase(BaseModel):
    loginCd:str
    

class LoginCreate(LoginBase):
    password: str

#for orm
class Login(LoginBase):
    id:int
    loginCd:str = Field(alias = 'login_cd')
    class Config:
        orm_mode = True