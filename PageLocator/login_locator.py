# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class LoginLocator:
    #账户登录iframe
    account_iframe = (By.XPATH,'//*[contains(@id,"x-URS-iframe")]')
    #用户名输入框
    username_input = (By.XPATH,'//input[@name="email"]')
    #密码输入框
    pwd_input = (By.XPATH,'//input[@name="password"]')
    #登录button
    login_button = (By.ID,'dologin')
    #注册button
    register_button = (By.ID,'changepage')
    #忘记密码链接
    #forget_link = (By.XPATH,'//a[@class="forgetpwd j-redirect"]')
    forget_link = (By.XPATH,'//div[@class="m-unlogin"]//a[@class="forgetpwd j-redirect"]')
    #未输入账号密码提示
    no_account = (By.XPATH,'//div[@id="nerror"]//div[@class="ferrorhead"]')
    #no_account = (By.XPATH,'//div[@class="ferrorhead"]')


