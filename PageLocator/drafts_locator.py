# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 14:26
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : MyLogger.py
# @Software: PyCharm Community Edition

from selenium.webdriver.common.by import By

class DraftsLocator:
    #今日草稿数量定位
    today_draft_count = (By.XPATH,'//div[@class="tb0 nn0"]//span[@class="nui-title-tips nui-txt-tips"]')