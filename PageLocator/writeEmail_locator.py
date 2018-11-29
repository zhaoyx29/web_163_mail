# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 14:26
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : MyLogger.py
# @Software: PyCharm Community Edition

from selenium.webdriver.common.by import By

class WriteEmailLocator:
    #首页tab
    index_tab = (By.XPATH,'//*[text()="首页"]')
    #草稿箱tab
    draft_tab = (By.XPATH,'//*[@class="js-component-tabitem tA0 oZ0 nui-tabs-item nui-tabs-item-selected rJ0"]')
    #写信tab
    writeEmail_tab = (By.XPATH,'//*[@class="js-component-tabitem tA0 nui-tabs-item nui-tabs-item-selected rJ0"]')
    #收件人输入框
    receive_input = (By.XPATH,'//input[@class="nui-editableAddr-ipt"]')
    #主题输入框
    subject_input = (By.XPATH,'//div[@class="kZ0 fu0"]//input')
    #写信输入框iframe
    content_input_iframe = (By.XPATH,'//*[@class="APP-editor-iframe"]')
    #写信iframe中输入框
    content_input = (By.XPATH,'//*[@class="nui-scroll"]')
    #【发送】button
    send_button = (By.XPATH,'//div[@class="nui-toolbar-item"]//span[text()="发送"]')
    #邮件发送成功的提示信息---发送状态
    sendEmail_success_msg = (By.XPATH,'//*[text()="发送成功"]')
    #抄送button
    copy_to_button = (By.XPATH,'//*[text()="抄送"]')
    #抄送人输入框
    copy_to_input = (By.XPATH,'//div[@class="kZ0 jL0cc"]//*[@class="nui-editableAddr-ipt"]')
    #【存草稿】button
    save_draft_button = (By.XPATH,'//*[text()="存草稿"]')
    #草稿保存成功提示
    save_draft_success_msg = (By.XPATH,'//div[@class="js-component-tips nui-frameTips nui-tips nui-tips-suc nui-frameTips-suc  "]//*[@class="nui-tips-text"]')
    #未填写收件人弹窗
    popup_withoutReceive = (By.XPATH,'//div[@class="js-component-tips nui-frameTips nui-tips "]//span[@class="nui-tips-text"]'
    )
    #未填写主题的提示信息
    without_subject_msg = (By.XPATH,'//div[@class="nui-msgbox-title"]')
    #未填写主题弹框的确定button
    without_subject_popup_button = (By.XPATH,'//div[@class="js-component-button nui-mainBtn nui-btn "]//span[@class="nui-btn-text"]')
    #添加附件链接
    add_attach_link = (By.XPATH,'//a[@class="cb0 nui-txt-link"]')