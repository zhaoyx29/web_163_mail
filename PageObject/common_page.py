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
        locator_dict = vars(CommonLocator)    #获取类的属性，并存为字典
        print(locator_dict)
        #遍历字典中的元素，若为元组，取元组中的第二个定位表达式的值，判断传入参数是否在表达式中，若存在,将该定位表达式传给click_ele()
        for i in (locator_dict.values()):
            if isinstance(i,tuple):
                if tab_name in i[1]:
                    self.wait_eleVisibility(i)
                    self.click_ele(i)

    def get_tabTitle(self,tab_name):
        name = '{0}获取页面tab的title'.format(tab_name)
        logger.info(name)
        locator_dict = vars(CommonLocator)    #获取类的属性，并存为字典
        print(locator_dict)
        #遍历字典中的元素，若为元组，取元组中的第二个定位表达式的值，判断传入参数是否在表达式中，若存在,将该定位表达式传给click_ele()
        for i in (locator_dict.values()):
            if isinstance(i,tuple):
                if tab_name in i[1]:
                    print(i)
                    self.wait_eleVisibility(i,model_name=name)
                    return self.get_text(i,model_name=name)

