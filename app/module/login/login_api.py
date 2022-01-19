# -*- coding: utf-8 -*-
# login.py
# @Author ouyang
# @Description  
# @Created  2022-01-11T10:27:06.528Z+08:00
# @Modified  2022-01-11T10:27:06.528Z+08:00
#

from fastapi.params import Depends
from sqlalchemy.orm import Session
from app.routers.router import apiRouter

from app.orm.common.database import get_db
from . import login_schemas
from . import service

@apiRouter.post('/login/', tags=["login"] )
async def login(item:login_schemas.LoginCreate, db:Session = Depends(get_db)):
  return service.login(item, db)

@apiRouter.post('/users/' , response_model=login_schemas.Login, tags=["login"])
async def registerUser(user: login_schemas.LoginCreate, db:Session = Depends(get_db)):
  return service.registerUser(user, db)