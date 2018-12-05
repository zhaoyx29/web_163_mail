# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 14:26
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : MyLogger.py
# @Software: PyCharm Community Edition

from Common.BasePage import BasePage
from Common.my_log import logger
from PageLocator.common_locator import CommonLocator

class CommonPage(CommonLocator,BasePage):
    #退出登录
    def quit_login(self):
        name="退出登录"
        logger.info(name)
        self.wait_eleVisibility(self.quit_button)
        self.click_ele(self.quit_button,model_name=name)

    def swtich_tab(self,tab_name):
        name="切换tab"
        logger.info(name)
        for locator in CommonLocator:

        for tab_name in locator[1]:
            self.click_ele(tab_name)

