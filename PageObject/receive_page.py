# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 14:26
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : MyLogger.py
# @Software: PyCharm Community Edition

from Common.BasePage import BasePage
from PageLocator.receive_locator import ReceiveLocator

class ReceivePage(ReceiveLocator,BasePage):
    def move_email(self,global_place):
        name='移动邮件到{0}'.format(global_place)
        self.wait_eleVisibility(self.move_to_button,model_name=name)
        self.click_ele(self.move_to_button,model_name=name)