# -*- coding: utf-8 -*-
from Common.BasePage import BasePage
from Common.MyLogger import *
from PageLocator.writeEmail_locator import WriteEmailLocator
from TestDatas.writeEmail_data import *

class WriteEmailPage(WriteEmailLocator,BasePage):
    def get_tabTitle(self):
        name = '获取写信tab的title'
        logging.info("获取写信页面的title")
        self.wait_eleVisibility(self.writeEmail_tab,model_name=name)
        return self.get_eleAttribute(self.writeEmail_tab,'title',model_name=name)

    def send_text_Email(self,receive,subject,content):
        name='发送文本信息邮件'
        logging.info('{0}'.format(name))
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

    def get_sendSuccess_msg(self):
        name="获取发送邮件成功的提示信息"
        logging.info(name)
        return self.get_text(self.sendEmail_success_msg,model_name=name)
