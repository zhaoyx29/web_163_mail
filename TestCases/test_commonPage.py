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

    def test_switch_tab_to_address_list(self,init_loginedEnv):
        logger.info( '切换到{0}tab中'.format(address_list_tab))
        CommonPage(init_loginedEnv).swtich_tab(address_list_tab)
        #断言
        try:
            assert CommonPage(init_loginedEnv).get_tabTitle(address_list_tab) == '通讯录'
        except AssertionError:
            logger.exception("断言出错啦：")
            raise

    def test_switch_tab_to_write(self,init_loginedEnv):
        logger.info( '切换到{0}tab中'.format(write_tab))
        CommonPage(init_loginedEnv).swtich_tab(write_tab)
        #断言
        try:
            assert CommonPage(init_loginedEnv).get_tabTitle(write_tab) == '写信'
        except AssertionError:
            logger.exception("断言出错啦：")
            raise


    def test_switch_tab_to_index(self,init_loginedEnv):
        logger.info( '切换到{0}tab中'.format(index_tab))
        CommonPage(init_loginedEnv).swtich_tab(index_tab)
        #断言
        try:
            assert CommonPage(init_loginedEnv).get_tabTitle(index_tab) == '首页'
        except AssertionError:
            logger.exception("断言出错啦：")
            raise