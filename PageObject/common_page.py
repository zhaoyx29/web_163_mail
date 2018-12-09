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

    def switch_tab(self,tab_name):
        name="切换到{0}tab".format(tab_name)
        logger.info(name)
        locator_dict = vars(CommonLocator)    #获取类的属性，并存为字典
        print(locator_dict)
        #遍历字典中的元素，若键名中包含字符串'tab',且该键的值为元组，则取元组中的第二个定位表达式的值，判断传入参数是否在表达式中，若存在,将该定位表达式传给click_ele()
        for k,i in (locator_dict.items()):
            if 'tab' in k and isinstance(i,tuple):
                if tab_name in i[1]:
                    self.wait_eleVisibility(i)
                    self.click_ele(i)

    #获取当前所在tab的title----除了特例：写信tab外，写信tab定位表达式和其余tab不一样
    def get_current_tab(self):
        name = '获取当前页面tab的title'
        logger.info(name)
        self.wait_eleVisibility(self.checked_tab)
        return self.get_text(self.checked_tab)

    def get_write_tabTitle(self):
        name='获取当前tab的文本信息'
        self.wait_eleVisibility(self.writeEmail_tab,model_name=name)
        self.move_IntoView(self.writeEmail_tab,model_name=name)
        return self.get_eleAttribute(self.writeEmail_tab,'title',model_name=name)


