'''
-*- coding:utf-8 -*-
@Author:WillowZhang
@Email:116995292@qq.com
@Time:2021/10/22  16:50
'''

import allure
import pytest
import scr.page.login_page
import scr.page.findwork_page
from scr.common.excel_util import read_excel


@allure.feature("找工作模块")
class TestFindWork():

    @allure.story("找工作模块测试")
    @allure.title("找工作测试用例01")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("点击搜索按钮，跳转搜索页面")
    @allure.step("点击搜索按钮，跳转搜索页面")
    def test_findwork_01(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.findwork_page.FindWorkPage(self.driver)
        value = wk.search_img()
        assert '搜索' == value

    @allure.story("找工作模块测试")
    @allure.title("找工作测试用例02")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("点击顶部【我的找活】按钮，跳转我的找活名片页")
    @allure.step("点击顶部【我的找活】按钮，跳转我的找活名片页")
    def test_findwork_02(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.findwork_page.FindWorkPage(self.driver)
        value = wk.search_my_work()
        assert '我的找活名片' == value

    @allure.story("找工作模块测试")
    @allure.title("找工作测试用例03")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("只选择城市，页面只展示该城市的招工信息")
    @allure.step("只选择城市，页面只展示该城市的招工信息")
    def test_findwork_03(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.findwork_page.FindWorkPage(self.driver)
        value = wk.choose_city()
        assert '晋中' == value

    @allure.story("找工作模块测试")
    @allure.title("找工作测试用例04")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("只选择工种，页面只展示该工种的招工信息")
    @allure.step("只选择工种，页面只展示该工种的招工信息")
    def test_findwork_04(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.findwork_page.FindWorkPage(self.driver)
        value = wk.choose_worktype()
        assert '安全员' == value

    @allure.story("找工作模块测试")
    @allure.title("找工作测试用例05")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("只选择其他选项，页面只展示实名的招工信息")
    @allure.step("只选择其他选项，页面只展示实名的招工信息")
    def test_findwork_05(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.findwork_page.FindWorkPage(self.driver)
        value = wk.choose_other()
        assert '实名' == value

    @allure.story("找工作模块测试")
    @allure.title("找工作测试用例06")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("发布招工")
    @allure.step('''1.点击发布招工
                    2.输入发布内容
                    3.点击确认发布，跳转完善信息页面
                    4.点击确认发布，发布成功''')
    def test_findwork_06(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.findwork_page.FindWorkPage(self.driver)
        value = wk.recruitment_information()
        assert '我发布的招工' == value