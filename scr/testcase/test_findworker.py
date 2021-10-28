'''
-*- coding:utf-8 -*-
@Author:WillowZhang
@Email:116995292@qq.com
@Time:2021/10/23  11:01
'''


import allure
import pytest
import scr.page.login_page
import scr.page.findworker_page
from scr.common.excel_util import read_excel


@allure.feature("找工人模块")
class TestFindWorker():


    @allure.story("找工人模块测试")
    @allure.title("找工人测试用例01")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("点击顶部【我的招工】按钮，跳转我发布的招工页")
    @allure.step("点击顶部【我的招工】按钮，跳转我发布的招工页")
    def test_findworker_01(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.findworker_page.FindWorkerPage(self.driver)
        value = wk.search_my_worker()
        assert '我发布的招工' == value

    @allure.story("找工人模块测试")
    @allure.title("找工人测试用例02")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("只选择城市，页面只展示该城市的找活信息")
    @allure.step("只选择城市，页面只展示该城市的找活信息")
    def test_findworker_02(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.findworker_page.FindWorkerPage(self.driver)
        value = wk.choose_city()
        assert '晋中' == value

    @allure.story("找工人模块测试")
    @allure.title("找工人测试用例03")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("只选择工种，页面只展示该工种的找活信息")
    @allure.step("只选择工种，页面只展示该工种的找活信息")
    def test_findworker_03(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.findworker_page.FindWorkerPage(self.driver)
        value = wk.choose_worktype()
        assert '安全员' == value

    @allure.story("找工人模块测试")
    @allure.title("找工人测试用例04")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("只选择其他选项，页面只展示实名的找活信息")
    @allure.step("只选择其他选项，页面只展示实名的找活信息")
    def test_findworker_04(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.findworker_page.FindWorkerPage(self.driver)
        value = wk.choose_other()
        assert '班组长' == value

    @allure.story("找工人模块测试")
    @allure.title("找工人测试用例05")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("点击【马上去置顶】，跳转置顶找活页面")
    @allure.step("点击【马上去置顶】，跳转置顶找活页面")
    def test_findworker_05(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.findworker_page.FindWorkerPage(self.driver)
        value = wk.top_my_card()
        assert '置顶找活' == value

    @allure.story("找工人模块测试")
    @allure.title("找工人测试用例06")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("编辑我的名片，修改工龄成功")
    @allure.step("编辑我的名片，修改工龄成功")
    def test_findworker_06(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.findworker_page.FindWorkerPage(self.driver)
        value = wk.modify_my_card()
        assert '我的找活名片' == value

    @allure.story("找工人模块测试")
    @allure.title("找工人测试用例07")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("点击【自我介绍】，跳转自我介绍添加页，输入文本，点击保存，保存成功")
    @allure.step("点击【自我介绍】，跳转自我介绍添加页，输入文本，点击保存，保存成功")
    def test_findworker_07(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.findworker_page.FindWorkerPage(self.driver)
        value = wk.edit_mytext()
        assert '细心' in value

    @allure.story("找工人模块测试")
    @allure.title("找工人测试用例08")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("点击【职业技能】，跳转职业技能添加页，输入文本，点击保存，保存成功")
    @allure.step("点击【职业技能】，跳转职业技能添加页，输入文本，点击保存，保存成功")
    def test_findworker_08(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.findworker_page.FindWorkerPage(self.driver)
        value = wk.edit_certificate()
        assert '职业技能' == value
