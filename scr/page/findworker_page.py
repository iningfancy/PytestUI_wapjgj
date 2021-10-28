'''
-*- coding:utf-8 -*-
@Author:WillowZhang
@Email:116995292@qq.com
@Time:2021/10/23  11:00
'''

from selenium.webdriver.common.by import By
from scr.common.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import time
import logging

class FindWorkerPage(BasePage):

    '''页面元素定位'''
    title_center = (By.CLASS_NAME, 'center')  # 顶部标题
    menu_find_worker = (By.XPATH, '//i[@class="iconfont iconzhaogongren"]')  # 菜单栏找工人
    my_work_top = (By.XPATH, '//*[@class="search"]//div[@class="right"]')  # 顶部我的招工按钮
    option = (By.XPATH, '//*[@class="van-ellipsis"]')  # 选项框
    frist_city = (By.XPATH, '//div[@class="province-item"]')  # 城市一级菜单
    second_city = (By.CLASS_NAME, "city-item")  # 城市二级菜单
    frist_work = (By.XPATH, '//*[@id="scrollBody"]/div[2]/div/div/div/div/div/div/div/div/div[1]/div[3]')  # 工种一级菜单
    second_work = (By.XPATH, '//*[@id="scrollBody"]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[4]')  # 工种二级菜单
    other_select = (By.XPATH, '//*[@id="scrollBody"]/div[2]/div/div/div/div/div/div/div/div/div[3]/div')  # 其它选项
    card_loc = (By.CLASS_NAME, 'fun')  # 名片选项
    top_card_loc = (By.XPATH, '//div[@class="top-right"]')      #置顶按钮
    eidt_data_loc = (By.CLASS_NAME,'check-tel')     #编辑资料
    worklength_loc = (By.XPATH,'//span[text()="工龄"]')     #编辑工龄
    work_age = (By.XPATH,'//input[@type="tel"]')    #工龄输入框
    goback_loc = (By.XPATH,'//*[@id="__layout"]/div/div/div/div[4]/div/div[1]/div[1]/div')    #返回
    save_loc = (By.XPATH,'//button[text()="保存"]')   #保存
    informations_loc = (By.XPATH, '//div[@class="edit"]')  # 自我介绍页信息选项
    my_text = (By.XPATH, '//textarea[@class="van-field__control"]')  # 自我介绍输入框
    eidt_text = (By.XPATH, '//*[@id="__layout"]/div/div/div/div[1]/div[3]/div[2]/span')  #自我介绍内容
    add_skills_loc = (By.CLASS_NAME, 'right')  # 添加
    add_skills_text = (By.XPATH, '//input[@type="text"]')  # 职能添加输入框


    '''页面动作'''
    def search_my_worker(self):
        self.click(self.menu_find_worker)
        time.sleep(1)
        self.click(self.my_work_top)
        time.sleep(1)
        center = self.locate_element(self.title_center).text     # 获取页面顶部文字：’我发布的招工‘
        return center

    def choose_city(self):
        self.click(self.menu_find_worker)
        time.sleep(3)
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
        self.click(self.menu_find_worker)
        time.sleep(3)
        options = self.loc_elements(self.option)
        time.sleep(1)
        options[1].click()
        time.sleep(5)
        self.click(self.frist_work)
        time.sleep(1)
        self.click(self.second_work)  # 选择到九大员-安全员
        time.sleep(2)
        worktypeB = self.loc_elements(self.option)
        worktype = worktypeB[1].text
        return worktype

    def choose_other(self):
        self.click(self.menu_find_worker)
        time.sleep(3)
        options = self.loc_elements(self.option)
        time.sleep(1)
        options[2].click()
        time.sleep(3)
        self.click(self.other_select)  # 选择到’班组长‘
        time.sleep(2)
        ortherB = self.loc_elements(self.option)
        orther = ortherB[2].text
        return orther

    def top_my_card(self):
        self.click(self.menu_find_worker)
        time.sleep(2)
        cards = self.loc_elements(self.card_loc)
        if len(cards) >= 1:
            cards[0].click()
        time.sleep(2)
        self.click(self.top_card_loc)
        time.sleep(1)
        center = self.locate_element(self.title_center).text     # 获取页面顶部文字：’置顶找活‘
        return center

    def modify_my_card(self):
        self.click(self.menu_find_worker)
        time.sleep(2)
        cards = self.loc_elements(self.card_loc)
        if len(cards) >= 1:
            cards[0].click()
        time.sleep(2)
        self.click(self.eidt_data_loc)
        time.sleep(1)
        self.click(self.worklength_loc)
        time.sleep(2)
        age = self.locate_element(self.work_age)  # 通过键盘全选，然后直接输入新的内容，就不用clear了
        age.send_keys((Keys.CONTROL, 'a'))
        time.sleep(1)
        self.send_keys(self.work_age, "5")
        time.sleep(1)
        self.click(self.goback_loc)
        time.sleep(1)
        self.click(self.save_loc)
        time.sleep(2)
        center = self.locate_element(self.title_center).text  # 获取页面顶部文字：’我的找活名片‘
        return center

    def edit_mytext(self):
        self.click(self.menu_find_worker)
        time.sleep(2)
        cards = self.loc_elements(self.card_loc)
        if len(cards) >= 1:
            cards[0].click()
        time.sleep(2)
        informations = self.loc_elements(self.informations_loc)
        if len(informations) >= 1:
            informations[0].click()
        time.sleep(3)
        qc = self.locate_element(self.my_text)
        qc.send_keys((Keys.CONTROL, 'a'))
        self.send_keys(self.my_text, "细心，热情")
        self.click(self.save_loc)
        time.sleep(2)
        center = self.locate_element(self.eidt_text).text  # 获取自我介绍文本内容
        return center

    def edit_certificate(self):
        self.click(self.menu_find_worker)
        time.sleep(2)
        cards = self.loc_elements(self.card_loc)
        if len(cards) >= 1:
            cards[0].click()
        time.sleep(2)
        informations = self.loc_elements(self.informations_loc)
        if len(informations) >= 1:
            informations[1].click()
        time.sleep(1)
        self.click(self.add_skills_loc)
        time.sleep(3)
        self.send_keys(self.add_skills_text, "高级技师证书")
        self.click(self.save_loc)
        time.sleep(3)
        center = self.locate_element(self.title_center).text  # 获取页面顶部文字：’职业技能‘
        return center