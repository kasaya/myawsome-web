# -*- coding: utf-8 -*-
# login_dao.py
# @Author ouyang
# @Description  
# @Created  2022-01-11T16:50:23.786Z+08:00
# @Modified  2022-01-11T16:50:23.786Z+08:00
#

from fastapi.params import Depends
from sqlalchemy.orm import Session
from app.orm.models.login_model import *
from typing import Optional
from app.orm.common import database

def get_login_info(login_cd: str, pwd: str, db:Session):
        pass
