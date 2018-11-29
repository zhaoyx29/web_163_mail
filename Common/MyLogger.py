# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 14:26
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : MyLogger.py
# @Software: PyCharm Community Edition

import logging
from Common.config_dir import *
from logging.handlers import RotatingFileHandler
import time

#定制日志输出格式
fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'

#指定输出的渠道1
handler_1 = logging.StreamHandler()

#指定输出的渠道2
curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())
handler_2 = RotatingFileHandler(logs_dir+"/Web_Autotest_{0}.log".format(curTime),encoding='utf-8')
#设置rootlogger 的输出内容形式，输出渠道
logging.basicConfig(format=fmt,datefmt=datefmt,level=logging.INFO,handlers=[handler_1,handler_2])
