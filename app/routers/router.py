# -*- coding: utf-8 -*-
# routers.py
# @Author ouyang
# @Description  
# @Created  2022-01-10T15:52:00.981Z+08:00
# @Modified  2022-01-10T17:09:23.399Z+08:00
#

from fastapi import APIRouter
apiRouter = APIRouter()

from app.module.common import main_page
from app.module.login import login_api


