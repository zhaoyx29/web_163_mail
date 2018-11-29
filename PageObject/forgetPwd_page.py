# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 14:26
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : MyLogger.py
# @Software: PyCharm Community Edition

from Common.BasePage import BasePage
from selenium.webdriver.common.by import By
#from Common.MyLogger import *
from Common.my_log import logger

class ForgetPwdPage(BasePage):

    def get_forgetUrl(self):
        logger.info('获取重置密码页面URL')
        return self.get_pageUrl()


    def input_email(self):
        self.wait_eleVisibility((By.XPATH,'//input[@class="ipt_input ipt_input_large ipt_input-success"]'),model_name='等待新窗口中元素可见')
        self.driver.find_element_by_xpath('//input[@class="ipt_input ipt_input_large ipt_input-success"]').send_keys('12')