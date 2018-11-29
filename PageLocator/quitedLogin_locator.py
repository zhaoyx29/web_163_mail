# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 6:18
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : quitedLogin_locator.py
# @Software: PyCharm Community Edition
from selenium.webdriver.common.by import By

class QuitePageLocator:
    #退出登录成功提示
    quitSuccess_msg =(By.XPATH,'//*[@class="info"]//h1')