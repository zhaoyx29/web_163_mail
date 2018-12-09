# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 14:26
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : MyLogger.py
# @Software: PyCharm Community Edition


from selenium.webdriver.common.by import By

class IndexLocator:
    #账户昵称
    account_nickname = (By.XPATH,'//span[@id="spnUid"]')
    #登录后的默认tab
    default_tab = (By.XPATH,'//*[@class="js-component-tabitem tA0 oZ0 nui-tabs-item qv0 nui-tabs-item-selected"]//div[@class="nui-tabs-item-text nui-fNoSelect"]')
    #菜单栏中收件箱
    receive_email = (By.XPATH,'//div[@class="js-component-component nui-tree-item-label nui-tree-item-label-selected"]//span[text()="收件箱"]')
    #【写信】button
    write_email = (By.XPATH,'//*[text()="写 信"]')
    #菜单栏中，草稿箱菜单定位
    drafts_menu = (By.XPATH,'//*[contains(@id,"_mail_component")]//*[text()="草稿箱"]')
    #菜单栏中，已发送菜单定位
    sended_menu = (By.XPATH,'//*[@class="js-component-component nui-tree-item-label"]//*[text()="已发送"]')