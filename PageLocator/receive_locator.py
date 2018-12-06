# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 14:26
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : MyLogger.py
# @Software: PyCharm Community Edition

from selenium.webdriver.common.by import By

class ReceiveLocator:
    #页面tab--收件箱
    tab_receive_mail = (By.ID,'//*[@class="js-component-tabitem tA0 oZ0 nui-tabs-item nui-tabs-item-selected"]//div[text()="收件箱"]')
    #【移动到】button
    move_to_button = (By.XPATH,'//span[text()="移动到"]')
    #【移动到】下拉列表中的草稿箱定位
    move_to_drafts = (By.XPATH,'//div[@class="nui-menu-item-link"]//span[text()="草稿箱"]')
    #【移动到】下拉列表中的已发送定位
    move_to_sended = (By.XPATH,'//div[@class="nui-menu-item-link"]//span[text()="已发送"]')
    #未选中邮件时，移动邮件
    move_withoutEmail = (By.XPATH,'//*[text()="没有选中任何邮件，请重新选择"]')