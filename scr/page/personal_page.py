'''
-*- coding:utf-8 -*-
@Author:WillowZhang
@Email:116995292@qq.com
@Time:2021/10/23  13:46
'''

from selenium.webdriver.common.by import By
from scr.common.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import time
import logging

class PersonalPage(BasePage):

    '''页面元素定位'''
    title_center = (By.CLASS_NAME, 'center')  # 顶部标题
    personal_center_loc = (By.XPATH, '//i[@class="iconfont iconwode"]')  # 个人中心按钮
    personal_data_loc = (By.LINK_TEXT,"个人资料")       #个人资料按钮
    gain_kgd_loc = (By.LINK_TEXT, "获取开工豆")      #获取开工豆按钮
    topup_loc = (By.XPATH,'//button[@class="recharge"]')        #充值按钮
    my_post_rec = (By.LINK_TEXT,'我的招工')     #我的招工
    look_mywork_loc = (By.XPATH, '//a[@href="/my/recruitmentBrowseRecord"]')      #谁看过我的招工
    look_mycard_loc = (By.XPATH, '//a[@href="/my/checkMyCard"]')        #谁看过我的名片
    refresh_mycard_loc = (By.XPATH, '//a[@href="/my/findJobCard"]')        #刷新名片
    check_details_loc = (By.XPATH, '//a[@href="/supervip"]')  # 查看超级会员详情
    feedback_loc = (By.XPATH,'//div[@to="/my/feedback"]')
    feedback_text = (By.XPATH, '//textarea[@rows="10"]')
    submit_loc = (By.XPATH, '//div[@class="submit-btn"]')
    locator = (By.XPATH, '//div[@class="van-toast__text"]')  # toast提示


    '''页面动作'''

    def personal_data(self):
        self.click(self.personal_center_loc)
        time.sleep(1)
        self.click(self.personal_data_loc)
        center = self.locate_element(self.title_center).text  # 获取页面顶部文字：’个人资料‘
        return center

    def gain_kgd(self):
        self.click(self.personal_center_loc)
        time.sleep(1)
        self.click(self.gain_kgd_loc)
        center = self.locate_element(self.title_center).text  # 获取页面顶部文字：’获取开工豆‘
        return center

    def topup_kgd(self):
        self.click(self.personal_center_loc)
        time.sleep(1)
        self.click(self.gain_kgd_loc)
        time.sleep(1)
        self.click(self.topup_loc)
        time.sleep(1)
        center = self.locate_element(self.title_center).text  # 获取页面顶部文字：’充值开工豆‘
        return center

    def post_rec(self):
        self.click(self.personal_center_loc)
        time.sleep(1)
        self.click(self.my_post_rec)
        time.sleep(1)
        center = self.locate_element(self.title_center).text  # 获取页面顶部文字：’我发布的招工‘
        return center

    def look_rec(self):
        self.click(self.personal_center_loc)
        time.sleep(1)
        self.click(self.look_mywork_loc)
        time.sleep(1)
        center = self.locate_element(self.title_center).text  # 获取页面顶部文字：’招工浏览记录‘
        return center

    def look_mycard(self):
        self.click(self.personal_center_loc)
        time.sleep(1)
        self.click(self.look_mycard_loc)
        time.sleep(1)
        center = self.locate_element(self.title_center).text  # 获取页面顶部文字：’谁看过我的名片‘
        return center

    def refresh_mycard(self):
        self.click(self.personal_center_loc)
        time.sleep(1)
        self.click(self.refresh_mycard_loc)
        time.sleep(1)
        center = self.locate_element(self.title_center).text  # 获取页面顶部文字：’我的找活名片‘
        return center

    def check_details(self):
        self.click(self.personal_center_loc)
        time.sleep(1)
        self.click(self.check_details_loc)
        time.sleep(1)
        center = self.locate_element(self.title_center).text  # 获取页面顶部文字：’超级会员‘
        return center

    def submit_feedback(self):
        self.click(self.personal_center_loc)
        time.sleep(1)
        self.click(self.feedback_loc)
        time.sleep(3)
        self.send_keys(self.feedback_text, "测试意见提交")
        time.sleep(1)
        self.click(self.submit_loc)
        time.sleep(5)
        toast_loc = self.locate_element(self.locator)
        text = toast_loc.get_attribute('textContent')  # 获取toast页面报错信息,反馈已提交，请登录吉工家APP查看处理结果
        return text