# -*- coding: utf-8 -*-
# @Time    : 2018/11/24 15:36
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : test_writeEmail.py
# @Software: PyCharm Community Edition

# import pytest
# from Common.MyLogger import *
# from TestDatas.writeEmail_data import *
# from PageObject.writeEmail_page import WriteEmailPage
#
# @pytest.mark.usefixtures("init_writeEnv")
# class TestWriteEmail:
#
#     def test_send_text_Email(self,init_writeEnv):
#         #步骤：发送邮件
#         WriteEmailPage(init_writeEnv).send_text_Email(send_textEmail_success['receive'],send_textEmail_success['subject'],send_textEmail_success['Email_content'])
#         #断言：是否有发送成功的提示
#         try:
#             assert WriteEmailPage(init_writeEnv).get_sendSuccess_msg() == send_textEmail_success['expected']
#         except AssertionError:
#             logging.exception('断言出错啦：')
#             raise
#

import pytest
from Common.my_log import logger
from TestDatas.writeEmail_data import *
from PageObject.writeEmail_page import WriteEmailPage
from PageObject.index_page import IndexPage
from PageObject.drafts_page import DraftsPage

@pytest.mark.usefixtures("init_writeEnv")
class TestWriteEmail:
    #发送纯文本邮件
    @pytest.mark.smoke
    def test_send_text_Email_ok(self,init_writeEnv):
        #步骤：发送邮件
        WriteEmailPage(init_writeEnv).send_text_Email(send_textEmail_success['receive'],send_textEmail_success['subject'],send_textEmail_success['Email_content'])
        #断言：是否有发送成功的提示
        try:
            assert WriteEmailPage(init_writeEnv).get_sendSuccess_msg() == send_textEmail_success['expected']
        except AssertionError:
            logger.exception('断言出错啦：')
            raise

    #存为草稿
    def test_save_draft(self,init_writeEnv):
        #点击存草稿button
        WriteEmailPage(init_writeEnv).save_draft()
        #断言--判断是否有邮件保存成功的提示信息
        try:
            assert '成功保存到草稿箱' in WriteEmailPage(init_writeEnv).get_saveDraft_success_msg()
        except AssertionError:
            logger.exception('断言出错啦')
            raise

    #发送附件邮件
    def test_send_attach_Email_ok(self,init_writeEnv):
        pass

    #发送附件+文本邮件
    def test_send_attachAndText_Email_ok(self,init_writeEnv):
        pass

    #发送邮件未填写收件人
    def test_send_Email_withoutReceive(self,init_writeEnv):
        #步骤：发送邮件---无收件人
        WriteEmailPage(init_writeEnv).send_text_Email(send_textEmail_withoutRecive['receive'],send_textEmail_withoutRecive['subject'],send_textEmail_withoutRecive['Email_content'])
        #断言：是否有正确的提示信息
        try:
            assert WriteEmailPage(init_writeEnv).get_withoutReceive_msg() == send_textEmail_withoutRecive['expected']
        except AssertionError:
            logger.exception('断言出错啦')
            raise

