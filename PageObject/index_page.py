# -*- coding: utf-8 -*-

from Common.MyLogger import *
from Common.BasePage import BasePage
from PageLocator.index_locator import IndexLocator


class IndexPage(IndexLocator,BasePage):

    def get_userAccount(self):
        name='index页面用户昵称'
        self.wait_eleVisibility(self.account_nickname,model_name=name)
        self.move_IntoView(self.account_nickname,model_name=name)
        return self.get_text(self.account_nickname,model_name=name)

    def get_msg_text(self,model_name=''):
        name='获取首页的{0}文本信息'.format(model_name)
        self.wait_eleVisibility(self.receive_email,model_name=name)
        self.move_IntoView(self.receive_email,model_name=name)
        return self.get_text(self.receive_email,model_name=name)

    def move_email(self,global_place):
        name='移动邮件到{0}'.format(global_place)
        self.wait_eleVisibility(self.move_to_button,model_name=name)
        self.click_ele(self.move_to_button,model_name=name)

    def go_writeEmail(self):
        name='进入写信页面'
        self.wait_eleVisibility(self.write_email,model_name=name)
        self.move_IntoView(self.write_email,model_name=name)
        self.click_ele(self.write_email,model_name=name)

    def quit_login(self):
        name="退出登录"
        logging.info(name)
        self.click_ele(self.quit_button,model_name=name)