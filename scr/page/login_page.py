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
import allure


class LoginPage(BasePage):

    current_url = "http://wap.jgjapp.com"
    '''页面元素定位'''
    homepage_popup_loc = (By.XPATH, '//div[@class="popup van-popup van-popup--center"]//div[@class="close"]')  # 页面弹窗
    boss_loc = (By.XPATH, '//div[@class="first-container"]//span[text()="老板"]')  # 我是老板
    worker_loc = (By.XPATH, '//div[@class="second-container"]//span[text()="干活的"]')  # 我是工人
    personal_center_loc = (By.XPATH, '//i[@class="iconfont iconwode"]')  # 个人中心按钮
    user_name_loc = (By.NAME, 'telph')  # 用户账号输入框
    verification_code_loc = (By.NAME, 'vcode')  # 验证码输入框
    login_button_loc = (By.XPATH, '//button[@type="submit"]')  # 登录按钮
    personal_center = (By.CLASS_NAME, 'center') #定位页面顶部文本
    locator = (By.XPATH,'//div[@class="van-toast__text"]') #toast提示
    top_find_worker = (By.XPATH, '//span[text()="找工人"]')  # 顶部找工人
    top_find_job = (By.XPATH, '//span[text()="找工作"]')  # 顶部找工作


    '''页面动作'''
    @allure.step("关闭首页弹窗")
    def close_popup(self):  # 进入首页，关闭弹窗
        self.click(self.homepage_popup_loc)  # 关闭弹窗
        logging.info('进入首页')  # 创建info日志
        self.click(self.personal_center_loc)  # 点击个人中心

    @allure.step("输入手机号：{1}，验证码：{2}")
    def login(self, phone,vcode):  # 登录页面
        allure.step("{0},{1}".format(phone,vcode))
        self.send_keys(self.user_name_loc,phone)  # 输入用户名
        self.send_keys(self.verification_code_loc,vcode)   # 输入验证码
        time.sleep(1)
        self.click(self.login_button_loc) # 点击登录按钮
        time.sleep(3)
        logging.info(f'{phone}登陆成功')  # 创建info日志

    def login_order(self,phone,vcode):  # 验证登录流程成功
        self.get_drive(self.current_url)
        time.sleep(2)
        self.close_popup()
        time.sleep(1)
        self.login(phone,vcode)
        self.click(self.personal_center_loc)  # 点击个人中心
        time.sleep(1)
        center=self.locate_element(self.personal_center).text # 获取页面顶部文字：’个人中心‘
        return center

    def login_fail(self, phone,vcode):  # 登录流程失败
        self.get_drive(self.current_url)
        time.sleep(2)
        self.close_popup()
        self.login(phone,vcode)
        time.sleep(2)
        toast_loc = self.locate_element(self.locator)   # 定位toast页面元素
        time.sleep(1)
        text = toast_loc.get_attribute('textContent')  # 获取toast页面报错信息
        return text

    def login_step(self,phone='18583773317',vcode='1101'): # 登录流程
        self.get_drive(self.current_url)
        self.close_popup()
        self.login(phone,vcode)

    @allure.step("只输入手机号，验证码为空")
    def phone_none(self, phone):  # 手机号为空
        self.get_drive(self.current_url)
        time.sleep(2)
        self.close_popup()
        self.send_keys(self.user_name_loc,phone)  # 输入用户名
        time.sleep(1)
        self.click(self.login_button_loc)  # 点击登录按钮
        time.sleep(1)
        center = self.locate_element(self.personal_center).text  # 获取页面顶部文字：’登录‘
        return center

    @allure.step("只输入验证码，手机号为空")
    def code_none(self,vcode):  # 验证码为空
        self.get_drive(self.current_url)
        time.sleep(2)
        self.close_popup()
        self.send_keys(self.verification_code_loc,vcode)   # 输入验证码
        time.sleep(1)
        self.click(self.login_button_loc)  # 点击登录按钮
        time.sleep(1)
        center = self.locate_element(self.personal_center).text  # 获取页面顶部文字：’登录‘
        return center

    @allure.step("点击首页弹窗-我是老板")
    def boss_popup(self):  # 点击我是老板跳转找工人页面
        self.get_drive(self.current_url)
        time.sleep(2)
        self.click(self.boss_loc)  # 关闭弹窗并跳转
        time.sleep(2)
        center = self.locate_element(self.top_find_worker).text  # 获取页面顶部文字：’找工人‘
        return center

    @allure.step("点击首页弹窗-我是干活的")
    def findjob_popup(self):  # 点击我是干活得跳转找工作页面
        self.get_drive(self.current_url)
        time.sleep(2)
        self.click(self.worker_loc)  # 关闭弹窗并跳转
        time.sleep(2)
        center = self.locate_element(self.top_find_job).text  # 获取页面顶部文字：’找工作‘
        return center


