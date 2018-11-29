# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 14:26
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : MyLogger.py
# @Software: PyCharm Community Edition

import pytest
#from Common.MyLogger import *
from Common.my_log import logger
from PageObject.index_page import IndexPage
from TestDatas.login_data import *
from TestDatas.common_data import *
from PageObject.forgetPwd_page import ForgetPwdPage

@pytest.mark.usefixtures("init_loginEnv")
class TestLogin:
    @pytest.mark.smoke
    def test_login_success(self,init_loginEnv):
        #输入用户名、密码，点击[登录]button
        init_loginEnv[1].login(login_success_data['username'],login_success_data['passwd'])
        #断言，比对结果
        try:
            assert IndexPage(init_loginEnv[0]).get_userAccount() == login_success_data['expected']
        except AssertionError:
            logger.exception('断言失败啦！')
            raise

    @pytest.mark.parametrize('data',login_noData)
    def test_login_noData(self,init_loginEnv,data):
        #不输入用户名或密码登录
        init_loginEnv[1].login(data['username'],data['passwd'])
        #断言
        try:
            assert init_loginEnv[1].get_login_noData_msg() == data['expected']
        except AssertionError:
            logger.exception('断言失败啦！')
            raise

    def test_goto_forgetPwdPage(self,init_loginEnv):
        #点击登录页面的【忘记密码】链接
        before_click_handles=init_loginEnv[0].window_handles
        init_loginEnv[1].goto_forgetPwd()
        #断言  ---页面是否打开（打开新窗口）
        try:
            init_loginEnv[1].wait_windows_and_switch_to_it(before_click_handles)   #调用wait_windows_and_switch_to_it方法，切换窗口，# 在测试用例中调用BasePage里的方法，是由页面对象去调用，该页面对象继承了BasePage类
            assert ForgetPwdPage(init_loginEnv[0]).get_forgetUrl() == forget_url
        except AssertionError:
            logger.exception('断言出错了')
            raise






