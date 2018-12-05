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

@pytest.mark.usefixtures("init_loginedEnv")
class TestCommonPage:
    def test_quit_login(self,init_loginedEnv):
        name = '退出登录'
        logger.info(name)
        #点击退出button
        CommonPage(init_loginedEnv).quit_login()
        #断言
        try:
            assert QuitePage(init_loginedEnv).get_quiteSuccess_msg() == '您已成功退出网易邮箱。'
        except AssertionError:
            logger.exception("断言出错啦：")
            raise

    def test_switch_tab(self,init_loginedEnv):
        CommonPage(init_loginedEnv).swtich_tab('首页')
        print('测试完成')
