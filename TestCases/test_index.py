# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 14:26
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : MyLogger.py
# @Software: PyCharm Community Edition

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



import pytest
import time
from Common.my_log import logger
from PageObject.index_page import IndexPage
from TestDatas.index_data import *
from PageObject.writeEmail_page import WriteEmailPage
from PageObject.common_page import CommonPage

@pytest.mark.usefixtures("init_loginedEnv")
class TestIndex:
    @pytest.mark.smoke
    def test_tab_name(self,init_loginedEnv):
        # 通过IndexPage页面对象来获取tab
        # name='进入首页页面，查看页面信息是否正确'
        # logger.info(name)
        # content=IndexPage(init_loginedEnv).get_tabTitle()
        # #断言
        # try:
        #     assert content == index_tab
        # except AssertionError:
        #     logger.exception('断言出错啦')
        #     raise
        # 通过CommonPage页面对象来获取tab
        name='进入首页页面，查看页面信息是否正确'
        logger.info(name)
        content=CommonPage(init_loginedEnv).get_tabTitle(index_tab)
        #断言
        try:
            assert content == index_tab
        except AssertionError:
            logger.exception('断言出错啦')
            raise

    def test_goto_writeEmail(self,init_loginedEnv):
        name = '进入写信页面'
        logger.info(name)
        #点击【写信】操作
        IndexPage(init_loginedEnv).goto_writeEmail()
        #比对当前是否在写信页面（tab）  当前title为：写信
        tab_title = CommonPage(init_loginedEnv).get_write_tabTitle()
        #断言
        try:
            assert tab_title == write_tab
        except AssertionError:
            logger.exception('断言出错啦')
            raise

    def test_goto_draft(self,init_loginedEnv):
        name = '进入草稿箱页面'
        logger.info(name)
        #点击【写信】操作
        IndexPage(init_loginedEnv).goto_drafts()
        #比对当前是否在草稿箱页面（tab）  当前title为：草稿箱
        tab_title = CommonPage(init_loginedEnv).get_current_tab()
        #断言
        try:
            assert tab_title == draft_tab
        except AssertionError:
            logger.exception('断言出错啦')
            raise

    # def test_goto_sended(self,init_loginedEnv):
    #     name = '进入已发送页面'
    #     logger.info(name)









