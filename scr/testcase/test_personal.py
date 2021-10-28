'''
-*- coding:utf-8 -*-
@Author:WillowZhang
@Email:116995292@qq.com
@Time:2021/10/23  13:46
'''

import allure
import pytest
import scr.page.login_page
import scr.page.personal_page
from scr.common.excel_util import read_excel


@allure.feature("个人中心模块")
class TestPersonalPage():


    @allure.story("个人中心模块测试")
    @allure.title("个人中心测试用例01")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("点击个人资料，跳转个人资料设置页")
    @allure.step("点击个人资料，跳转个人资料设置页")
    def test_personal_01(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.personal_page.PersonalPage(self.driver)
        value = wk.personal_data()
        assert '个人资料' == value

    @allure.story("个人中心模块测试")
    @allure.title("个人中心测试用例02")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("点击【获取开工豆】，跳转获取开工豆页面")
    @allure.step("点击【获取开工豆】，跳转获取开工豆页面")
    def test_personal_02(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.personal_page.PersonalPage(self.driver)
        value = wk.gain_kgd()
        assert '获取开工豆' == value

    @allure.story("个人中心模块测试")
    @allure.title("个人中心测试用例03")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("“获取开工豆”-点击【直接去充值】，跳转充值开工豆页面")
    @allure.step("“获取开工豆”-点击【直接去充值】，跳转充值开工豆页面")
    def test_personal_03(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.personal_page.PersonalPage(self.driver)
        value = wk.topup_kgd()
        assert '充值开工豆' == value

    @allure.story("个人中心模块测试")
    @allure.title("个人中心测试用例04")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("点击【我的招工】，跳转我发布的招工页面")
    @allure.step("点击【我的招工】，跳转我发布的招工页面")
    def test_personal_04(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.personal_page.PersonalPage(self.driver)
        value = wk.post_rec()
        assert '我发布的招工' == value

    @allure.story("个人中心模块测试")
    @allure.title("个人中心测试用例05")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("点击【谁看过我的招工】，跳转招工浏览记录页面")
    @allure.step("点击【谁看过我的招工】，跳转招工浏览记录页面")
    def test_personal_05(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.personal_page.PersonalPage(self.driver)
        value = wk.look_rec()
        assert '招工浏览记录' == value

    @allure.story("个人中心模块测试")
    @allure.title("个人中心测试用例06")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("点击【谁看过我的名片】，谁看过我的名片")
    @allure.step("点击【谁看过我的名片】，谁看过我的名片")
    def test_personal_06(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.personal_page.PersonalPage(self.driver)
        value = wk.look_mycard()
        assert '谁看过我的名片' == value

    @allure.story("个人中心模块测试")
    @allure.title("个人中心测试用例07")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("点击【刷新名片】，跳转我的找活名片")
    @allure.step("点击【刷新名片】，跳转我的找活名片")
    def test_personal_07(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.personal_page.PersonalPage(self.driver)
        value = wk.refresh_mycard()
        assert '我的找活名片' == value

    @allure.story("个人中心模块测试")
    @allure.title("个人中心测试用例08")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("“我是超级会员”点击【查看详情】，跳转超级会员页面")
    @allure.step("“我是超级会员”点击【查看详情】，跳转超级会员页面")
    def test_personal_08(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.personal_page.PersonalPage(self.driver)
        value = wk.check_details()
        assert '超级会员' == value

    @allure.story("个人中心模块测试")
    @allure.title("个人中心测试用例09")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("点击【意见反馈】，填写意见内容，点击提交,提交成功")
    @allure.step("点击【意见反馈】，填写意见内容，点击提交,提交成功")
    def test_personal_09(self):
        lp = scr.page.login_page.LoginPage(self.driver)
        lp.login_step()
        wk = scr.page.personal_page.PersonalPage(self.driver)
        value = wk.submit_feedback()
        assert '反馈已提交，请登录吉工家APP查看处理结果' == value
