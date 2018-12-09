# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 9:36
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : test_commonPage.py
# @Software: PyCharm Community Edition
import pytest
from Common.my_log import logger
from PageObject.common_page import CommonPage
from PageObject.quitedLogin_page import QuitePage
from TestDatas.commonPage_data import *

@pytest.mark.usefixtures("init_loginedEnv")
class TestCommonPage:
    def test_quit_login(self,init_loginedEnv):
        logger.info('退出登录')
        #点击退出button
        CommonPage(init_loginedEnv).quit_login()
        #断言
        try:
            assert QuitePage(init_loginedEnv).get_quiteSuccess_msg() == '您已成功退出网易邮箱。'
        except AssertionError:
            logger.exception("断言出错啦：")
            raise

    # def test_switch_tab_to_address_list(self,init_loginedEnv):
    #     logger.info( '切换到{0}tab中'.format(address_list_tab))
    #     CommonPage(init_loginedEnv).switch_tab(address_list_tab)
    #     #断言
    #     try:
    #         assert CommonPage(init_loginedEnv).get_tabTitle(address_list_tab) == '通讯录'
    #     except AssertionError:
    #         logger.exception("断言出错啦：")
    #         raise

    @pytest.mark.parametrize('data',switch_tab_data)
    def test_switch_tab(self,init_loginedEnv,data):
        logger.info( '切换到{0}tab中'.format(data['tab_name']))
        CommonPage(init_loginedEnv).switch_tab(data['tab_name'])
        #断言
        try:
            assert CommonPage(init_loginedEnv).get_tabTitle(data['tab_name']) == data['expected']
        except AssertionError:
            logger.exception("断言出错啦：")
            raise