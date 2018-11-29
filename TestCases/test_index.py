# -*- coding: utf-8 -*-
# import pytest
# from Common.MyLogger import *
# from PageObject.index_page import IndexPage
# from PageObject.writeEmail_page import WriteEmailPage
# from PageObject.quitedLogin_page import QuitePage

# @pytest.mark.usefixtures("init_indexEnv")
# class TestIndex:
#     def test_check_receive_mail_list(self,init_indexEnv):
#         name='进入收件箱页面，查看收件箱列表'
#         logging.info("进入收件箱页面，查看收件箱列表")
#         content=IndexPage(init_indexEnv).get_msg_text(name)
#         #断言
#         try:
#             assert content == '收件箱'
#         except AssertionError:
#             logging.exception('断言出错啦')
#             raise
#
#     def test_goto_writeEmail(self,init_indexEnv):
#         name = '进入写信页面'
#         logging.info(name)
#         #点击【写信】操作
#         IndexPage(init_indexEnv).go_writeEmail()
#         #断言
#         #比对当前是否在写信页面（tab）  当前title为：写信
#         tab_title = WriteEmailPage(init_indexEnv).get_tabTitle()
#         try:
#             assert tab_title == '写信'
#         except AssertionError:
#             logging.exception('断言错误：')
#             raise
#
#     def test_quit_login(self,init_indexEnv):
#         name = '退出登录'
#         logging.info(name)
#         #点击退出button
#         IndexPage(init_indexEnv).quit_login()
#         #断言
#         try:
#             assert QuitePage(init_indexEnv).get_quiteSuccess_msg() == '您已成功退出网易邮箱。'
#         except AssertionError:
#             logging.exception("断言出错啦：")
#             raise
#
#

import pytest
from Common.my_log import logger
from PageObject.index_page import IndexPage
from PageObject.writeEmail_page import WriteEmailPage
from PageObject.quitedLogin_page import QuitePage

@pytest.mark.usefixtures("init_indexEnv")
class TestIndex:
    def test_check_receive_mail_list(self,init_indexEnv):
        name='进入收件箱页面，查看收件箱列表'
        logger.info("进入收件箱页面，查看收件箱列表")
        content=IndexPage(init_indexEnv).get_msg_text(name)
        #断言
        try:
            assert content == '收件箱'
        except AssertionError:
            logger.exception('断言出错啦')
            raise

    def test_goto_writeEmail(self,init_indexEnv):
        name = '进入写信页面'
        logger.info(name)
        #点击【写信】操作
        IndexPage(init_indexEnv).go_writeEmail()
        #断言
        #比对当前是否在写信页面（tab）  当前title为：写信
        tab_title = WriteEmailPage(init_indexEnv).get_tabTitle()
        try:
            assert tab_title == '写信'
        except AssertionError:
            logger.exception('断言错误：')
            raise

    def test_quit_login(self,init_indexEnv):
        name = '退出登录'
        logger.info(name)
        #点击退出button
        IndexPage(init_indexEnv).quit_login()
        #断言
        try:
            assert QuitePage(init_indexEnv).get_quiteSuccess_msg() == '您已成功退出网易邮箱。'
        except AssertionError:
            logger.exception("断言出错啦：")
            raise





