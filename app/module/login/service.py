# -*- coding: utf-8 -*-
# service.py
# @Author ouyang
# @Description  
# @Created  2022-01-11T17:19:21.886Z+08:00
# @Modified  2022-01-11T17:19:21.886Z+08:00
#

from typing import Optional
from sqlalchemy.orm.session import Session

from app.excetpion.customer_exception import AppcationExcetpion
from app.orm.models.login_model import *
from . import login_schemas  
import hashlib
from app.utils.log_util import *




def login(item: login_schemas.LoginCreate, db:Session):
   logger.debug("进入登录方法")
   filelogger.debug("file进入登录方法")
   loginCdinfo:Optional[Login] = db.query(Login).filter(Login.login_cd == item.loginCd).first()
   logger.info("执行方法")
   filelogger.debug("file执行方法")
   if loginCdinfo:
      pwd:Optional[Login]= db.query(Login).filter(Login.hashed_password == md5Password(item.password)).first()
      if pwd:
            return {'result': 'welcome ! %s' % item.loginCd}
   return {'result': 'sorry !'}

def registerUser(user:login_schemas.LoginCreate, db:Session):
   count:int = db.query(Login).filter(Login.login_cd == user.loginCd).count()
   if count > 0:
      raise AppcationExcetpion('999','userExist','用户已经存在')
   #加密密码
   db_login = Login(login_cd = user.loginCd, hashed_password = md5Password(user.password))
   db.add(db_login)
   db.commit()
   #刷新db_login对象
   db.refresh(db_login)
   return db_login

def md5Password(pwd:str)->str:
   hash = hashlib.md5()
   hash.update(pwd.encode(encoding='utf-8'))
   return hash.hexdigest()
    