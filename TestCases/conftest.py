# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from TestDatas.common_data import *
from PageObject.login_page import LoginPage
from PageObject.index_page import IndexPage

@pytest.fixture
def init_loginEnv():
    #启动浏览器静默模式
    # option = webdriver.ChromeOptions()
    # option.add_argument('headless')
    # driver = webdriver.Chrome(chrome_options=option)
    driver=webdriver.Chrome()
    driver.get(login_url)
    #窗口最大化
    driver.maximize_window()
    LoginP=LoginPage(driver)
    LoginP.wait_iframe_and_switch_to_it(LoginP.account_iframe,model_name='切换到登录iframe')   #调用wait_windows_and_switch_to_it方法，切换窗口，# 在测试用例中调用BasePage里的方法，是由页面对象去调用，该页面对象继承了BasePage类
    yield [driver,LoginP]
    driver.quit()

@pytest.fixture
def init_indexEnv():
    #启动浏览器静默模式
    # option = webdriver.ChromeOptions()
    # option.add_argument('headless')
    # driver = webdriver.Chrome(chrome_options=option)
    driver=webdriver.Chrome()
    driver.get(login_url)
    #窗口最大化
    driver.maximize_window()
    LoginP=LoginPage(driver)
    LoginP.wait_iframe_and_switch_to_it(LoginP.account_iframe)
    LoginP.login(login_data['username'],login_data['passwd'])
    yield driver
    driver.quit()

@pytest.fixture
def init_writeEnv():
    #启动浏览器静默模式
    # option = webdriver.ChromeOptions()
    # option.add_argument('headless')
    # driver = webdriver.Chrome(chrome_options=option)
    driver=webdriver.Chrome()
    driver.get(login_url)
    #窗口最大化
    driver.maximize_window()
    LoginP=LoginPage(driver)
    LoginP.wait_iframe_and_switch_to_it(LoginP.account_iframe)
    LoginP.login(login_data['username'],login_data['passwd'])
    IndexPage(driver).go_writeEmail()
    yield driver
    #driver.quit()