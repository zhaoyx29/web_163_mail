# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 14:26
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : MyLogger.py
# @Software: PyCharm Community Edition

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

# driver=webdriver.Chrome()
# driver.get("https://mail.163.com/")
#
# # ele=driver.find_element_by_xpath('//*[contains(@id,"x-URS-iframe")]')
# # WebDriverWait(driver,20).until(EC.frame_to_be_available_and_switch_to_it(ele))
#
# #切换到登录iframe弹窗
# WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[contains(@id,"x-URS-iframe")]')))
# driver.switch_to.frame(driver.find_element_by_xpath('//*[contains(@id,"x-URS-iframe")]'))   #通过webdriver对象切换
# #输入用户名密码
# driver.find_element_by_xpath('//input[@name="email"]').send_keys('zhaotester')
# driver.find_element_by_xpath('//input[@name="password"]').send_keys('yx.920929')
# #窗口切换
# # cur_handles1=driver.window_handles
# # print('cur_handles1:',cur_handles1)
#
# #点击忘记密码，切换到新窗口
# # driver.find_element_by_xpath('//a[@class="forgetpwd j-redirect"]').click()
# #窗口切换
# # WebDriverWait(driver,20).until(EC.new_window_is_opened(cur_handles1))
# # cur_handles=driver.window_handles
# # driver.switch_to.window(cur_handles[-1])
# # driver.find_element_by_xpath('//input[@class="ipt_input ipt_input_large ipt_input-success"]').send_keys('12')
#
# #点击登录
# driver.find_element_by_id('dologin').click()
#
# # WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.XPATH,'//span[contains(@id,"dvGreetName")]')))
# # a=driver.find_element_by_xpath('//span[contains(@id,"dvGreetName")]').text
#
# #登录以后点击【写信】
# locator='//*[text()="写 信"]'
# WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.XPATH,'//*[text()="写 信"]')))
# driver.find_element_by_xpath('//*[text()="写 信"]').click()
#
# #切换到文本输入框iframe，输入发送的内容
# ele = driver.find_element_by_xpath('//*[@class="APP-editor-iframe"]')
# WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it(ele))
# driver.find_element_by_xpath('//*[@class="nui-scroll"]').send_keys('sss')
# #切换出iframe，点击发送
# driver.switch_to.default_content()
# driver.find_element_by_xpath('//div[@class="nui-toolbar-item"]//span[text()="发送"]')
#
# # #1.获取新打开tab的title
# # t=driver.find_element_by_xpath('//*[@class="js-component-tabitem tA0 nui-tabs-item nui-tabs-item-selected rJ0"]').get_attribute('title')
# # print(t)
#


import pytest
from selenium import webdriver
from TestDatas.base_data import *
from TestDatas.base_data import *
from PageObject.login_page import LoginPage
from PageObject.index_page import IndexPage
from Common.BasePage import BasePage
from PageLocator.common_locator import *
def swtich_tab(tab_name):
    #启动浏览器静默模式
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=option)
    #driver=webdriver.Chrome()
    driver.get(login_url)
    #窗口最大化
    driver.maximize_window()
    LoginP=LoginPage(driver)
    LoginP.wait_iframe_and_switch_to_it(LoginP.account_iframe)
    LoginP.login(login_data['username'],login_data['passwd'])

    locator_dict = vars(CommonLocator)    #获取类的属性，并存为字典
    print(locator_dict)
    #遍历字典中的元素，若为元组，取元组中的第二个定位表达式的值，判断传入参数是否在表达式中，若存在,将该定位表达式传给click_ele()
    for i in (locator_dict.values()):
        if isinstance(i,tuple):
            if tab_name in i[1]:
                BasePage(driver).wait_eleVisibility(i)
                BasePage(driver).click_ele(i)


swtich_tab('首页')