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
        locator = []
        for i,value in vars(CommonLocator).items():
            locator.append(i)
        print(locator)
        if tab_name in locator[1]:
            self.click_ele(locator[0])
        else:
            print(locator)


#  2 class Market(object):
#  3   def __init__(self):
#  4     self.title = 'apple'
#  5     self.count = '20'
#  6   def list_all_member(self):
#  7     for name,value in vars(self).items():
#  8       print('%s=%s'%(name,value))
#  9 if __name__== '__main__':
# 10   market= Market()
# 11   market.list_all_member()
