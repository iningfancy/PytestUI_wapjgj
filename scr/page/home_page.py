'''
-*- coding:utf-8 -*-
@Author:WillowZhang
@Email:116995292@qq.com
@Time:2021/10/21  16:52
'''

from selenium.webdriver.common.by import By
from scr.common.base_page import BasePage
import time
import logging

class HomePage(BasePage):

    '''页面元素定位'''
    work_title = (By.XPATH,'//*[@id="scrollBody"]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div')  #列表招工信息第一个
    search_frist_work = (By.XPATH,'//*[@id="scrollBody"]/div[3]/div/div[1]/div[1]/div/a/h2/span')   #搜索工作定位
    search_frist_worker = (By.XPATH, '//*[@id="scrollBody"]/div[4]/div/div[1]/a/div/div/div[1]/div[1]/div[2]/div[1]/h1')  # 搜索工人定位
    title_center = (By.CLASS_NAME, 'center')    #顶部标题
    construction = (By.LINK_TEXT,'建筑招工')    #建筑招工按钮
    decorate = (By.LINK_TEXT,'装修招工')    #装修招工按钮
    welders = (By.LINK_TEXT,'焊工招聘')    #焊工招聘按钮
    Courier = (By.LINK_TEXT,'工厂/快递')    #工厂/快递按钮
    work_types = (By.XPATH,'//*[@id="scrollBody"]/div[2]/div/div/div/ul/li[2]/div')    #选择工种选项框
    my_work_top = (By.XPATH, '//*[@class="custom-header"]//div[@class="right"]')    #顶部我的找活按钮
    my_work_bottom = (By.LINK_TEXT, '我的找活')  # 底部我的找活按钮
    menu_find_work =(By.XPATH, '//i[@class="iconfont iconzhaogongzuo"]')    #菜单栏找工作
    menu_find_worker = (By.XPATH, '//i[@class="iconfont iconzhaogongren"]')     #菜单栏找工人
    top_find_work = (By.XPATH, '//span[text()="找工作"]')      #顶部找工作
    top_find_worker = (By.XPATH, '//span[text()="找工人"]')    #顶部找工人
    city_select = (By.XPATH, '//*[@class="van-ellipsis"]')      #首页城市选项框
    frist_city = (By.CLASS_NAME, "province-item")       #城市一级菜单
    second_city = (By.CLASS_NAME, "city-item")      #城市二级菜单
    find_body = (By.XPATH, '//input[@type="search"]')   #搜索框
    search_button = (By.XPATH, '//div[text()="搜索"]')   #搜索页-搜索按钮
    shear_work = (By.XPATH, '//img[@alt="分享"]')  # 分享
    Qr_code = (By.XPATH, '//div[text()="长按二维码保存"]')  # 吉工家 招工找活


    '''页面动作'''
    def work_information(self):
        self.click(self.work_title)
        time.sleep(2)
        center = self.locate_element(self.title_center).text# 获取页面顶部文字：’招工详情‘
        return center

    def click_construction(self):
        self.click(self.construction)
        time.sleep(2)
        select_list = self.locate_element(self.work_types)
        work_type = select_list.text
        return work_type

    def click_decorate(self):
        self.click(self.decorate)
        time.sleep(2)
        select_list = self.locate_element(self.work_types)
        work_type = select_list.text
        return work_type

    def click_welders(self):
        self.click(self.welders)
        time.sleep(2)
        select_list = self.locate_element(self.work_types)
        work_type = select_list.text
        return work_type

    def click_Courier(self):
        self.click(self.Courier)
        time.sleep(2)
        select_list = self.locate_element(self.work_types)
        work_type = select_list.text
        return work_type

    def top_mywork_information(self):
        self.click(self.my_work_top)
        time.sleep(2)
        center = self.locate_element(self.title_center).text    # 获取页面顶部文字：’我的找活名片‘
        return center

    def bottom_mywork_information(self):
        self.click(self.my_work_bottom)
        time.sleep(2)
        center = self.locate_element(self.title_center).text    # 获取页面顶部文字：’我的找活名片‘
        return center

    def find_work(self):
        self.click(self.menu_find_work)
        time.sleep(2)
        center = self.locate_element(self.top_find_work).text   # 获取页面顶部文字：’找工作‘
        return center

    def find_worker(self):
        self.click(self.menu_find_worker)
        time.sleep(2)
        center = self.locate_element(self.top_find_worker).text     # 获取页面顶部文字：’找工人‘
        return center

    def select_citys(self):
        self.click(self.city_select)
        time.sleep(6)
        frist_cs = self.loc_elements(self.frist_city)
        if len(frist_cs) >= 1:
            frist_cs[4].click()
        second_cs = self.loc_elements(self.second_city)
        if len(second_cs) >= 1:
            second_cs[7].click()        #选择到山西省-晋中市
        city = self.locate_element(self.city_select).text       # 获取城市选项框内容：’晋中‘
        return city

    def search_input(self):
        self.click(self.find_body)
        time.sleep(2)
        center = self.locate_element(self.title_center).text     # 获取页面顶部文字：’搜索‘
        return center

    def search_work(self,content):
        self.click(self.find_body)
        self.send_keys(self.find_body,content)
        time.sleep(5)
        self.click(self.search_button)
        title = self.locate_element(self.search_frist_work).text    #获取搜索的工作第一个标题
        return title

    def search_worker(self,content):
        self.click(self.find_body)
        self.click(self.top_find_worker)
        time.sleep(2)
        self.send_keys(self.find_body,content)
        self.click(self.search_button)
        time.sleep(5)
        title = self.locate_element(self.search_frist_worker).text      #获取搜索的工人第一个姓名
        return title


