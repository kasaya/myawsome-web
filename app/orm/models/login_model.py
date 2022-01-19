# -*- coding: utf-8 -*-
# login_model.py
# @Author ouyang
# @Description  
# @Created  2022-01-11T16:04:59.374Z+08:00
# @Modified  2022-01-11T16:04:59.374Z+08:00
#

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.sql.sqltypes import VARCHAR
from app.orm.common.database import Base

class Login(Base):
    __tablename__ = "login"

    id = Column(Integer, primary_key=True, index=True)
    login_cd = Column(String)
    hashed_password =Column(String)
