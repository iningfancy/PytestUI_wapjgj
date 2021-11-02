'''
-*- coding:utf-8 -*-
@Author:WillowZhang
@Email:116995292@qq.com
@Time:2021/10/19  13:54
'''
import logging
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self,driver):
        self.driver = driver
        # mobileEmulation = {"deviceName": "iPhone X"}
        # # Chrome使用手机调试模式显示
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option('mobileEmulation', mobileEmulation)
        # self.driver = webdriver.Chrome(options=options)


    #加载网页
    def get_drive(self,url):
        # 打开目标的网址
        self.driver.get(url)
        logging.info(f'登录{url}网站') #创建info日志

    #定位元素
    def locate_element(self,args):
        return self.driver.find_element(*args)

    #定位一组元素
    def loc_elements(self,args):
        return self.driver.find_elements(*args)

    #设置值
    def send_keys(self,args,value):
        self.locate_element(args).send_keys(value)

    #单击
    def click(self,args):
        self.locate_element(args).click()



# if __name__ == '__main__':
#      BasePage().get_drive()

