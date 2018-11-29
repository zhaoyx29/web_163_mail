# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 14:26
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : MyLogger.py
# @Software: PyCharm Community Edition


import pytest
import time

pytest.main(["-m","smoke","--reruns","2",r"--html=Reports\{0}_report.html".format(time.strftime("%Y%m%d_%H%M%S"))])
