# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 14:26
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : MyLogger.py
# @Software: PyCharm Community Edition

import logging
import time
from Common.config_dir import *
from logging.handlers import RotatingFileHandler

class Logger:

    def set_logger(self):

        fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
        datefmt = '%a, %d %b %Y %H:%M:%S'

        handler_1 = logging.StreamHandler()
        handler_2 = RotatingFileHandler(logs_dir+'//Web_Auto_{0}.log'.format(time.strftime("%Y-%m-%d %H%M",time.localtime())),encoding='utf-8')

        logging.basicConfig(format=fmt,datefmt=datefmt,level=logging.INFO,handlers=[handler_1,handler_2])
        return logging

logger = Logger().set_logger()
