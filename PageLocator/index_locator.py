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
    #收件箱
    receive_email = (By.XPATH,'//div[@id="_mail_component_67_67"]//span[text()="收件箱"]')
    #页面tab--收件箱
    tab_receive_mail = (By.ID,'_mail_tabitem_13_185text')
    #【写信】button
    write_email = (By.XPATH,'//*[text()="写 信"]')
    #退出登录button
    quit_button = (By.XPATH,'//a[text()="退出"]')
    #菜单栏中，草稿箱菜单定位
    drafts_menu = (By.XPATH,'//div[@class="js-component-component nui-tree-item-label"]//*[text()="草稿箱"]')