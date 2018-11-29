# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 14:26
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : MyLogger.py
# @Software: PyCharm Community Edition

from Common.BasePage import BasePage
#from Common.MyLogger import *
from Common.my_log import logger
from PageLocator.writeEmail_locator import WriteEmailLocator

class WriteEmailPage(WriteEmailLocator,BasePage):
    def get_tabTitle(self):
        name = '获取写信tab的title'
        logger.info("获取写信页面的title")
        self.wait_eleVisibility(self.writeEmail_tab,model_name=name)
        return self.get_eleAttribute(self.writeEmail_tab,'title',model_name=name)

    #发送文本邮件
    def send_text_Email(self,receive,subject,content):
        name='发送文本信息邮件'
        logger.info('{0}'.format(name))
        self.wait_eleVisibility(self.receive_input)
        #步骤
        #输入收件人
        self.input_keys(self.receive_input,receive)
        #输入主题
        self.input_keys(self.subject_input,subject)
        #输入邮件正文---切换到文本输入iframe----输入文本
        self.wait_iframe_and_switch_to_it(self.content_input_iframe,model_name=name)
        self.input_keys(self.content_input,content)
        #从iframe中切换出来，点击发送
        self.driver.switch_to.default_content()
        self.click_ele(self.send_button,model_name=name)

    #获取发送成功的消息
    def get_sendSuccess_msg(self):
        name="获取发送邮件成功的提示信息"
        logger.info(name)
        return self.get_text(self.sendEmail_success_msg,model_name=name)

    #发送附件邮件
    def send_attach_Email(self):
        pass

    def goto_index_tab(self):
        name="点击【首页】tab，跳转至首页"
        logger.info(name)
        self.click_ele(self.index_tab)

    #存草稿
    def save_draft(self):
        name="将邮件存为草稿"
        logger.info(name)
        self.move_IntoView(self.save_draft_button)
        self.click_ele(self.save_draft_button,model_name=name)

    #获取草稿保存成功的提示信息
    def get_saveDraft_success_msg(self):
        name="获取草稿保存成功的提示信息"
        logger.info(name)
        self.wait_eleVisibility(self.save_draft_success_msg,model_name=name)
        return self.get_text(self.save_draft_success_msg,model_name=name)

    def get_withoutReceive_msg(self):
        name="获取未输入收件人时，发送邮件的提示信息"
        logger.info(name)
        self.wait_eleVisibility(self.popup_withoutReceive,model_name=name)
        return self.get_text(self.popup_withoutReceive,model_name=name)



