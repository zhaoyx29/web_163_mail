# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 14:26
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : MyLogger.py
# @Software: PyCharm Community Edition

from selenium.webdriver.common.by import By

class CommonLocator:
    #退出登录button
    quit_button = (By.XPATH,'//a[text()="退出"]')
    #被选中的tab定位
    checked_tab = (By.XPATH,'//*[@class="js-component-tabitem tA0 oZ0 nui-tabs-item nui-tabs-item-selected"]//div[@class="nui-tabs-item-text nui-fNoSelect"]')
    #首页tab
    unselected_tab = (By.XPATH,'//*[text()="首页"]')
    #通讯录tab
    address_list_tab = (By.XPATH,'//*[text()="通讯录"]')
    #应用中心
    application_center_tab = (By.XPATH,'//*[text()="应用中心"]')
    #草稿箱
    drafts_tab = (By.XPATH,'//*[text()="草稿箱"]')
    #已发送
    sended_tab = (By.XPATH,'//*[text()="已发送"]')
    #写信tab
    writeEmail_tab = (By.XPATH,'//*[text()="写信"]')



