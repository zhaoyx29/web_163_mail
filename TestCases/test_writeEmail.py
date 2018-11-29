# -*- coding: utf-8 -*-
# @Time    : 2018/11/24 15:36
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : test_writeEmail.py
# @Software: PyCharm Community Edition
import pytest
from Common.MyLogger import *
from TestDatas.writeEmail_data import *
from PageObject.writeEmail_page import WriteEmailPage

@pytest.mark.usefixtures("init_writeEnv")
class TestWriteEmail:

    def test_send_text_Email(self,init_writeEnv):
        #步骤：发送邮件
        WriteEmailPage(init_writeEnv).send_text_Email(send_textEmail_success['receive'],send_textEmail_success['subject'],send_textEmail_success['Email_content'])
        #断言：是否有发送成功的提示
        try:
            assert WriteEmailPage(init_writeEnv).get_sendSuccess_msg() == send_textEmail_success['expected']
        except AssertionError:
            logging.exception('断言出错啦：')
            raise


