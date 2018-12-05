# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 6:20
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : quitedLogin_page.py
# @Software: PyCharm Community Edition
from Common.BasePage import BasePage
from Common.my_log import logger
from PageLocator.quitedLogin_locator import QuitePageLocator


class QuitePage(QuitePageLocator,BasePage):
    def get_quiteSuccess_msg(self):
        name="获取退出成功信息"
        logger.info(name)
        return self.get_text(self.quitSuccess_msg,model_name=name)
