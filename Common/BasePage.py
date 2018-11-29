# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 14:26
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : MyLogger.py
# @Software: PyCharm Community Edition

import time
#from Common.MyLogger import *
from Common.my_log import logger
from Common.config_dir import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def find_ele(self,locator,model_name=''):
        """
        :param locator: 类型为元组(By.XXX,定位表达式)
        :param filename:截图存放位置
        """
        #异常捕获，失败时，添加日志和截图
        try:
            logger.info('查找元素_{0}'.format(model_name))
            return self.driver.find_element(*locator)
        except:
            logger.exception('查找元素失败')
            self._get_screenShot(model_name)
            raise

    def find_eles(self,locator,model_name=''):
        """
        :param locator: 类型为元组(By.XXX,定位表达式)
        :param filename:截图存放位置
        """
        #异常捕获，失败时，添加日志和截图
        try:
            logger.info('查找元素_{0}'.format(model_name))
            return self.driver.find_elements(*locator)
        except:
            logger.exception('查找元素失败')
            self._get_screenShot(model_name)
            raise


    def input_keys(self,locator,content,model_name=''):
        ele = self.find_ele(locator,model_name)
        try:
            logger.info('{0}-输入文本'.format(model_name))
            ele.send_keys(content)
        except:
            logger.exception('输入文本操作失败')
            self._get_screenShot(model_name)
            raise

    def click_ele(self,locator,model_name=''):
        ele = self.find_ele(locator)
        try:
            logger.info('{0}-点击操作'.format(model_name))
            ele.click()
        except:
            logger.exception('点击元素操作失败')
            self._get_screenShot(model_name)
            raise

    def wait_windows_and_switch_to_it(self,current_handles,wait_time=20,poll_frequency=0.5,model_name=''):
        try:
            logger.info('等待新窗口打开')
            WebDriverWait(self.driver,wait_time,poll_frequency).until(EC.new_window_is_opened(current_handles))
        except:
            logger.exception('等待打开新窗口失败')
            self._get_screenShot(model_name)
            raise
        try:
            logger.info('切换到新打开的窗口')
            cur_handles = self.driver.window_handles
            self.driver.switch_to.window(cur_handles[-1])
        except:
            logger.exception('切换到新打开的窗口失败')
            self._get_screenShot(model_name)
            raise

    def wait_iframe_and_switch_to_it(self,locator,wait_time=20,poll_frequency=0.5,model_name=''):
        """
        :param locator: 类型为元组(By.XXX,iframe的定位表达式),
        """
        ele = self.find_ele(locator)
        try:
            logger.info('等待并且换到iframe-{0}'.format(model_name))
            WebDriverWait(self.driver,wait_time,poll_frequency).until(EC.frame_to_be_available_and_switch_to_it(ele))
        except:
            logger.exception('等待并且换到iframe失败')
            self._get_screenShot(model_name)
            raise

    def wait_eleVisibility(self,locator,wait_time=20,poll_frequency=0.5,model_name=''):
        try:
            logger.info('等待{0}中元素可见'.format(model_name))
            WebDriverWait(self.driver,wait_time,poll_frequency).until(EC.visibility_of_element_located(locator))
        except:
            logger.exception('等待元素可见失败')
            self._get_screenShot(model_name)
            raise

    def move_IntoView(self,locator,model_name=''):
        ele = self.find_ele(locator)
        try:
            logger.info('将{0}的元素移动到可见区域'.format(model_name))
            self.driver.execute_script("arguments[0].scrollIntoView()",ele)
        except:
            logger.exception('将元素移动到可见区域失败')
            self._get_screenShot(model_name)
            raise


    def get_text(self,locator,model_name=''):
        ele = self.find_ele(locator)
        try:
            logger.info('获取{0}文本信息'.format(model_name))
            return ele.text
        except:
            logger.exception('获取当前文本信息失败')
            self._get_screenShot(model_name)
            raise

    def get_eleAttribute(self,locator,attribute,model_name=''):
        ele = self.find_ele(locator)
        try:
            logger.info('获取{0}的元素属性'.format(model_name))
            return ele.get_attribute(attribute)
        except:
            logger.exception('获取元素属性失败')
            self._get_screenShot(model_name)
            raise

    def get_pageUrl(self,model_name=''):
        try:
            return self.driver.current_url
        except:
            logger.exception('获取页面URL失败')
            self._get_screenShot(model_name)
            raise

    def _get_screenShot(self,model_name):
        screen_path=screenShot_dir + '\\{0}_{1}.png'.format(model_name,time.strftime("%Y%m%d_%H%M%S"))
        try:
            self.driver.get_screenshot_as_file(screen_path)
            logger.info('截图成功，截图为：',screen_path)
        except:
            logger.exception('截图操作失败')
            raise


