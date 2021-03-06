# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 14:26
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : MyLogger.py
# @Software: PyCharm Community Edition

#from Common.MyLogger import *
from Common.my_log import logger
from Common.BasePage import BasePage
from PageLocator.index_locator import IndexLocator


class IndexPage(IndexLocator,BasePage):

    def get_userAccount(self):
        name='index页面用户昵称'
        self.wait_eleVisibility(self.account_nickname,model_name=name)
        self.move_IntoView(self.account_nickname,model_name=name)
        return self.get_text(self.account_nickname,model_name=name)

    def get_current_tabTitle(self):
        name='获取当前tab的文本信息'
        self.wait_eleVisibility(self.default_tab,model_name=name)
        self.move_IntoView(self.default_tab,model_name=name)
        return self.get_text(self.default_tab,model_name=name)

    def goto_writeEmail(self):
        name='进入写信页面'
        self.wait_eleVisibility(self.write_email,model_name=name)
        self.move_IntoView(self.write_email,model_name=name)
        self.click_ele(self.write_email,model_name=name)

    def goto_drafts(self):
        name="进入草稿箱列表"
        logger.info(name)
        self.wait_eleVisibility(self.drafts_menu,model_name=name)
        self.click_ele(self.drafts_menu,model_name=name)

    def goto_sended(self):
        name = "进入已发送列表"
        logger.info(name)
        self.wait_eleVisibility(self.sended_menu,model_name=name)
        self.click_ele(self.sended_menu,model_name=name)