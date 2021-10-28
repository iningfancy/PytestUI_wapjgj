'''
-*- coding:utf-8 -*-
@Author:WillowZhang
@Email:116995292@qq.com
@Time:2021/10/22  16:42
'''

from selenium.webdriver.common.by import By
from scr.common.base_page import BasePage
import time
import logging

class FindWorkPage(BasePage):

    '''页面元素定位'''
    find_body = (By.XPATH, '//img[@src="/_nuxt/img/search.9ed5ee7.png"]')   #搜索框
    title_center = (By.CLASS_NAME, 'center')    #顶部标题
    menu_find_work = (By.XPATH, '//i[@class="iconfont iconzhaogongzuo"]')  # 菜单栏找工作
    my_work_top = (By.XPATH, '//*[@class="search"]//div[@class="right"]')    #顶部我的找活按钮
    option = (By.XPATH, '//*[@class="van-ellipsis"]')  # 选项框
    frist_city = (By.XPATH, '//div[@class="province-item"]')       #城市一级菜单
    second_city = (By.CLASS_NAME, "city-item")      #城市二级菜单
    frist_work = (By.XPATH, '//*[@id="scrollBody"]/div[2]/div/div/div/div/div/div/div/div/div[1]/div[3]')  # 工种一级菜单
    second_work = (By.XPATH, '//*[@id="scrollBody"]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[4]')  # 工种二级菜单
    other_select = (By.XPATH, '//*[@id="scrollBody"]/div[2]/div/div/div/div/div/div/div/div/div[2]')  # 其它选项
    publish_work_loc = (By.LINK_TEXT, '发布招工')  # 发布招工
    content = (By.CLASS_NAME,'van-field__control')
    publish_send = (By.XPATH, '//button[text()="确认发布"]')
    choose_work = (By.XPATH, '//input[@placeholder="请选择工种"]')
    choose_place = (By.XPATH, '//input[@placeholder="请选择项目所在地"]')
    choose_pcity = (By.XPATH,'//*[@id="__layout"]/div/div/div/div[6]/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div/input')
    one_work = (By.XPATH, '//*[@id="__layout"]/div/div/div/div[4]/div/div[2]/div[1]/div[3]')  # 发布页工种一级菜单
    two_work = (By.XPATH, '//*[@id="__layout"]/div/div/div/div[4]/div/div[2]/div[2]/div[1]')  # 发布页工种二级菜单
    third_city = (By.CLASS_NAME, "area-item")    #发布页城市三级菜单

    '''页面动作'''
    def search_img(self):
        self.click(self.menu_find_work)
        time.sleep(1)
        self.click(self.find_body)
        time.sleep(1)
        center = self.locate_element(self.title_center).text     # 获取页面顶部文字：’搜索‘
        return center

    def search_my_work(self):
        self.click(self.menu_find_work)
        time.sleep(1)
        self.click(self.my_work_top)
        time.sleep(1)
        center = self.locate_element(self.title_center).text     # 获取页面顶部文字：’我的找活名片‘
        return center

    def choose_city(self):
        self.click(self.menu_find_work)
        time.sleep(1)
        options = self.loc_elements(self.option)
        time.sleep(1)
        options[0].click()
        time.sleep(5)
        frist_cs = self.loc_elements(self.frist_city)
        if len(frist_cs) >= 1:
            frist_cs[4].click()
        second_cs = self.loc_elements(self.second_city)
        if len(second_cs) >= 1:
            second_cs[7].click()  # 选择到山西省-晋中市
        time.sleep(2)
        cityB = self.loc_elements(self.option)
        city = cityB[0].text
        return city

    def choose_worktype(self):
        self.click(self.menu_find_work)
        time.sleep(1)
        options = self.loc_elements(self.option)
        time.sleep(1)
        options[1].click()
        time.sleep(6)
        self.click(self.frist_work)
        time.sleep(2)
        self.click(self.second_work)  # 选择到九大员-安全员
        time.sleep(2)
        worktypeB = self.loc_elements(self.option)
        worktype = worktypeB[1].text
        return worktype

    def choose_other(self):
        self.click(self.menu_find_work)
        time.sleep(1)
        options = self.loc_elements(self.option)
        time.sleep(1)
        options[2].click()
        time.sleep(3)
        self.click(self.other_select) # 选择到实名
        time.sleep(2)
        ortherB = self.loc_elements(self.option)
        orther = ortherB[2].text
        return orther

    def recruitment_information(self):
        self.click(self.publish_work_loc)
        time.sleep(3)
        self.send_keys(self.content,"测试-发布招工信息")
        self.click(self.publish_send)
        self.click(self.choose_work)
        time.sleep(5)
        self.click(self.one_work)
        self.click(self.two_work)
        self.click(self.choose_place)
        time.sleep(3)
        self.click(self.choose_pcity)
        time.sleep(3)
        frist_cs = self.loc_elements(self.frist_city)
        if len(frist_cs) >= 1:
            frist_cs[8].click()
        second_cs = self.loc_elements(self.second_city)
        if len(second_cs) >= 1:
            second_cs[0].click()  # 选择到上海市-静安区
        third_cs = self.loc_elements(self.third_city)
        third_cs[4].click()
        self.click(self.publish_send)
        time.sleep(5)
        center = self.locate_element(self.title_center).text  # 获取页面顶部文字：’我发布的招工‘
        return center