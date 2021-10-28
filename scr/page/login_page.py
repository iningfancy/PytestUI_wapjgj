'''
-*- coding:utf-8 -*-
@Author:WillowZhang
@Email:116995292@qq.com
@Time:2021/10/18  16:40
'''
from selenium.webdriver.common.by import By
from scr.common.base_page import BasePage
import time
import logging


class LoginPage(BasePage):

    current_url = "http://wap.jgjapp.com"
    '''页面元素定位'''
    homepage_popup_loc = (By.XPATH, '//div[@class="popup van-popup van-popup--center"]//div[@class="close"]')  # 页面弹窗
    personal_center_loc = (By.XPATH, '//i[@class="iconfont iconwode"]')  # 个人中心按钮
    user_name_loc = (By.NAME, 'telph')  # 用户账号输入框
    verification_code_loc = (By.NAME, '验证码')  # 验证码输入框
    login_button_loc = (By.XPATH, '//button[@type="submit"]')  # 登录按钮
    personal_center = (By.CLASS_NAME, 'center') #定位页面顶部文本
    locator = (By.XPATH,'//div[@class="van-toast__text"]') #toast提示


    '''页面动作'''
    def close_popup(self):  # 进入首页，关闭弹窗
        self.click(self.homepage_popup_loc)  # 关闭弹窗
        logging.info('进入首页')  # 创建info日志
        self.click(self.personal_center_loc)  # 点击个人中心

    def login(self, phone, code):  # 登录页面
        self.send_keys(self.user_name_loc,phone)  # 输入用户名
        self.send_keys(self.verification_code_loc,code)   # 输入验证码
        time.sleep(1)
        self.click(self.login_button_loc) # 点击登录按钮
        time.sleep(3)
        logging.info(f'{phone}登陆成功')  # 创建info日志

    def login_order(self,phone, code):  # 验证登录流程成功
        self.get_drive(self.current_url)
        self.close_popup()
        self.login(phone, code)
        self.click(self.personal_center_loc)  # 点击个人中心
        time.sleep(1)
        center=self.locate_element(self.personal_center).text #获取页面顶部文字：’个人中心‘
        return center

    def login_fail(self, phone, code):  # 登录流程失败
        self.get_drive(self.current_url)
        self.close_popup()
        self.login(phone, code)
        time.sleep(3)
        toast_loc = self.locate_element(self.locator)
        text = toast_loc.get_attribute('textContent')  # 获取toast页面报错信息
        return text

    def login_step(self,phone='18583773317',code='1101'): #登录流程
        self.get_drive(self.current_url)
        self.close_popup()
        self.login(phone, code)

