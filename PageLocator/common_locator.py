# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 14:26
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : MyLogger.py
# @Software: PyCharm Community Edition

from selenium.webdriver.common.by import By

class CommonLocator:
    #页面tab-首页
    index_tab = (By.XPATH,'//*[text()="首页"]')
    #页面tab--收件箱、草稿箱、已发送等菜单中元素定位
    tab_name = (By.XPATH,'//*[@class="js-component-tabitem tA0 oZ0 nui-tabs-item nui-tabs-item-selected"]//div[@class="nui-tabs-item-text nui-fNoSelect"]')
    #页面tab--草稿箱
    draft_tab = (By.XPATH,'//*[@class="js-component-tabitem tA0 oZ0 nui-tabs-item nui-tabs-item-selected rJ0"]')
    #页面tab--写信
    writeEmail_tab = (By.XPATH,'//*[@class="js-component-tabitem tA0 nui-tabs-item nui-tabs-item-selected rJ0"]')
    #页面tab--通讯录
    address_book_tab = (By.XPATH,'//*[@class="js-component-tabitem tA0 oZ0 nui-tabs-item nui-tabs-item-selected"]//div[@class="nui-tabs-item-text nui-fNoSelect"]')