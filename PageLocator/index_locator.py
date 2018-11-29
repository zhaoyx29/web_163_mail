# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

class IndexLocator:
    #账户昵称
    account_nickname = (By.XPATH,'//span[@id="spnUid"]')
    #收件箱
    receive_email = (By.XPATH,'//div[@id="_mail_component_67_67"]//span[text()="收件箱"]')
    #页面tab--收件箱
    tab_receive_mail = (By.ID,'_mail_tabitem_13_185text')
    #【移动到】button
    move_to_button = (By.XPATH,'//span[text()="移动到"]')
    #【移动到】下拉列表中的草稿箱定位
    move_to_drafts = (By.XPATH,'//div[@class="nui-menu-item-link"]//span[text()="草稿箱"]')
    #【移动到】下拉列表中的已发送定位
    move_to_sended = (By.XPATH,'//div[@class="nui-menu-item-link"]//span[text()="已发送"]')
    #未选中邮件时，移动邮件
    move_withoutEmail = (By.XPATH,'//*[text()="没有选中任何邮件，请重新选择"]')
    #【写信】button
    write_email = (By.XPATH,'//*[text()="写 信"]')
    #退出登录button
    quit_button = (By.XPATH,'//a[text()="退出"]')