'''
-*- coding:utf-8 -*-
@Author:WillowZhang
@Email:116995292@qq.com
@Time:2021/10/21  18:10
'''

import allure
import pytest
import scr.page.login_page
import scr.page.home_page
from scr.common.excel_util import read_excel


@allure.feature("首页模块")
class TestHomePage():

    @allure.story("首页模块测试")
    @allure.title("首页测试用例01")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("进入首页，点击招工信息，可进入招工详情页")
    @allure.step("进入首页，点击招工信息，可进入招工详情页")
    def test_homepage_01(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.home_page.HomePage(self.driver)
        value = wk.work_information()
        assert '招工详情' == value

    @allure.story("首页模块测试")
    @allure.title("首页测试用例02")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("首页-点击【建筑招工】，成功进入建筑招工页面，只展示建筑类招工")
    @allure.step("首页-点击【建筑招工】，成功进入建筑招工页面，只展示建筑类招工")
    def test_homepage_02(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.home_page.HomePage(self.driver)
        value = wk.click_construction()
        assert '建筑木工/铝模/二次结构' == value

    @allure.story("首页模块测试")
    @allure.title("首页测试用例03")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("首页-点击【装修招工】，成功进入装修招工页面，只展示装修类招工")
    @allure.step("首页-点击【装修招工】，成功进入装修招工页面，只展示装修类招工")
    def test_homepage_03(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.home_page.HomePage(self.driver)
        value = wk.click_decorate()
        assert '装修木工/吊顶/木地板' == value

    @allure.story("首页模块测试")
    @allure.title("首页测试用例04")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("首页-点击【焊工招聘】，成功进入焊工招聘页面，只展示焊工类招工")
    @allure.step("首页-点击【焊工招聘】，成功进入焊工招聘页面，只展示焊工类招工")
    def test_homepage_04(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.home_page.HomePage(self.driver)
        value = wk.click_welders()
        assert '焊工/铆工/钣金/钳工' == value

    @allure.story("首页模块测试")
    @allure.title("首页测试用例05")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("首页-点击【工厂/快递】，成功进入工厂/快递页面，只展示工厂/快递类招工")
    @allure.step("首页-点击【工厂/快递】，成功进入工厂/快递页面，只展示工厂/快递类招工")
    def test_homepage_05(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.home_page.HomePage(self.driver)
        value = wk.click_Courier()
        assert '工厂普工' == value

    @allure.story("首页模块测试")
    @allure.title("首页测试用例06")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("点击顶部【我的找活】按钮，跳转我的找活名片页")
    @allure.step("点击顶部【我的找活】按钮，跳转我的找活名片页")
    def test_homepage_06(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.home_page.HomePage(self.driver)
        value = wk.top_mywork_information()
        assert '我的找活名片' == value

    @allure.story("首页模块测试")
    @allure.title("首页测试用例07")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("点击底部【我的找活】按钮，跳转我的找活名片页")
    @allure.step("点击底部【我的找活】按钮，跳转我的找活名片页")
    def test_homepage_07(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.home_page.HomePage(self.driver)
        value = wk.bottom_mywork_information()
        assert '我的找活名片' == value

    @allure.story("首页模块测试")
    @allure.title("首页测试用例08")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("点击菜单栏【找工作】，切换至找工作页面")
    @allure.step("点击菜单栏【找工作】，切换至找工作页面")
    def test_homepage_08(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.home_page.HomePage(self.driver)
        value = wk.find_job()
        assert '找工作' == value

    @allure.story("首页模块测试")
    @allure.title("首页测试用例09")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("点击菜单栏【找工人】，切换至找工人页面")
    @allure.step("点击菜单栏【找工人】，切换至找工人页面")
    def test_homepage_09(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.home_page.HomePage(self.driver)
        value = wk.find_worker()
        assert '找工人' == value

    @allure.story("首页模块测试")
    @allure.title("首页测试用例10")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("点击搜索框切换城市，可切换成功")
    @allure.step("点击搜索框切换城市，可切换成功")
    def test_homepage_10(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.home_page.HomePage(self.driver)
        value = wk.select_citys()
        assert '晋中' == value

    @allure.story("首页模块测试")
    @allure.title("首页测试用例11")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("点击搜索输入框，跳转搜索页面")
    @allure.step("点击搜索输入框，跳转搜索页面")
    def test_homepage_11(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.home_page.HomePage(self.driver)
        value = wk.search_input()
        assert '搜索' == value

    @allure.story("首页模块测试")
    @allure.title("首页测试用例12")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("找工作-输入搜索内容，点击搜索，成功展示标题包含输入内容的搜索内容")
    @pytest.mark.parametrize('caseinfo', read_excel("./data/data.xlsx", "search1"))
    def test_homepage_12(self,caseinfo):
        index, case_name, content, is_exe, result = caseinfo
        allure.dynamic.description(case_name)
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.home_page.HomePage(self.driver)
        value = wk.search_work(content)
        assert content in value

    @allure.story("首页模块测试")
    @allure.title("首页测试用例13")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("找工人-输入搜索内容，点击搜索，成功展示姓名匹配正确的搜索内容")
    @pytest.mark.parametrize('caseinfo', read_excel("./data/data.xlsx", "search2"))
    def test_homepage_13(self,caseinfo):
        index, case_name, content, is_exe, result = caseinfo
        allure.dynamic.description(case_name)
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.home_page.HomePage(self.driver)
        value = wk.search_worker(content)
        assert content in value