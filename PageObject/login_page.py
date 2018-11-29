# -*- coding: utf-8 -*-

from PageLocator.login_locator import LoginLocator
from Common.BasePage import BasePage

class LoginPage(LoginLocator,BasePage):

    def login(self,username,pwd):
        #定位到用户名密码输入iframe,并且换到该frame
        operate_name='登录页面-输入用户名密码'
        #定位iframe中的用户名密码输入框
        self.wait_eleVisibility(self.username_input,model_name=operate_name)
        self.move_IntoView(self.username_input,model_name=operate_name)
        self.input_keys (self.username_input,username,model_name=operate_name)
        self.input_keys(self.pwd_input,pwd,model_name=operate_name)
        #定位登录button
        click_button_name='登录页面-点击登录button'
        self.move_IntoView(self.login_button,model_name=click_button_name)
        self.click_ele(self.login_button,click_button_name)

    def goto_register(self):
        click_button_name='登录页面-点击注册button'
        self.move_IntoView(self.register_button)
        self.click_ele(self.register_button,click_button_name)

    def goto_forgetPwd(self):
        click_link_name='登录页面-点击忘记密码link'
        self.wait_eleVisibility(self.forget_link,model_name=click_link_name)
        self.move_IntoView(self.forget_link)
        self.click_ele(self.forget_link,click_link_name)

    def get_login_noData_msg(self):
        noData_msg_name='登录页面-获取无用户名或密码的文本'
        self.wait_eleVisibility(self.no_account,wait_time=30,model_name=noData_msg_name)
        self.move_IntoView(self.no_account,model_name=noData_msg_name)
        return self.get_text(self.no_account,model_name=noData_msg_name)

