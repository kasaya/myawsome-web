# -*- coding: utf-8 -*-
# homepage.py
# @Author ouyang
# @Description  
# @Created  2022-01-10T15:54:59.284Z+08:00
# @Modified  2022-01-10T15:56:39.478Z+08:00
#

from app.routers.router import apiRouter

@apiRouter.get("/", tags=["main"])
async def homepage():
    return {"index": "homepage"}

@apiRouter.get("/about", tags=["main"])
async def about():
    return {"index": "about"}

