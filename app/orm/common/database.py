# -*- coding: utf-8 -*-
# database.py
# @Author ouyang
# @Description  
# @Created  2022-01-11T14:50:48.298Z+08:00
# @Modified  2022-01-11T14:50:48.298Z+08:00
#

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from typing import Optional
from app.utils.read_config import ReadConfig

rc = ReadConfig()
SQLALCHEMY_DATABASE_URL = rc.get_config("sql.url")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

session_factory:sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db:Session = session_factory()
    try:
        yield db
    finally:
        db.close()   
   
