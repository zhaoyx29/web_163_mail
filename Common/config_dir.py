# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 14:26
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : MyLogger.py
# @Software: PyCharm Community Edition

import os

#项目基础路径
base_dir=os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
#print(base_dir)
#日志路径
logs_dir=os.path.join(base_dir,'Logs')
#print(logs_dir)
#测试报告路径
report_dir=os.path.join(base_dir,'Reports')
#截图路径
screenShot_dir=os.path.join(base_dir,'ScreenShots')
#测试用例路径
testcase_dir=os.path.join(base_dir,'TestCases')
