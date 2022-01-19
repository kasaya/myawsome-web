# -*- coding: utf-8 -*-
# log_util.py
# @Author ouyang
# @Description  
# @Created  2022-01-18T14:21:34.704Z+08:00
# @Modified  2022-01-18T14:21:34.704Z+08:00
#

import logging
from logging import Logger, config
import yaml

with open('./config/logging.yml', 'r') as file:
     logging_yaml:dict = yaml.load(file.read(), Loader=yaml.FullLoader)
     config.dictConfig(config = logging_yaml)

logger:Logger = logging.getLogger("simpleExample")
filelogger:Logger = logging.getLogger("filelogger")