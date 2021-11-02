'''
-*- coding:utf-8 -*-
@Author:WillowZhang
@Email:116995292@qq.com
@Time:2021/10/18  15:46
'''
import time

import allure
import pytest
import scr.page.login_page
from scr.common.excel_util import read_excel

@allure.feature("登录模块")
class TestLogin():

    @allure.story("登录模块测试")
    @allure.title("正确的手机号验证，登陆成功")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('caseinfo',read_excel("./data/data_login.xlsx","login"))
    def test_login_01(self,caseinfo):
        index,case_name,phone,vcode,is_exe,result = caseinfo
        #加上用例描述
        allure.dynamic.description(case_name)
        lp = scr.page.login_page.LoginPage(self.driver)
        value = lp.login_order(phone,vcode)
        assert '个人中心' == value
        # print(value)

    @allure.story("登录模块测试")
    @allure.title("错误手机号或验证码验证")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('caseinfo',read_excel("./data/data_login.xlsx","login_fail"))
    def test_login_02(self,caseinfo):
        index,case_name,phone,vcode,is_exe,result = caseinfo
        #加上用例描述
        allure.dynamic.description(case_name)
        lp = scr.page.login_page.LoginPage(self.driver)
        value = lp.login_fail(phone,vcode)
        assert '输入' in value

    @allure.story("登录模块测试")
    @allure.title("验证码为空，不可登陆")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('caseinfo',read_excel("./data/data_login.xlsx","phone_none"))
    def test_login_03(self,caseinfo):
        index,case_name,phone,is_exe,result = caseinfo
        #加上用例描述
        allure.dynamic.description(case_name)
        lp = scr.page.login_page.LoginPage(self.driver)
        value = lp.phone_none(phone)
        assert '登录' == value

    @allure.story("登录模块测试")
    @allure.title("手机号为空，不可登陆")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('caseinfo',read_excel("./data/data_login.xlsx","vcode_none"))
    def test_login_04(self,caseinfo):
        index,case_name,vcode,is_exe,result = caseinfo
        #加上用例描述
        allure.dynamic.description(case_name)
        lp = scr.page.login_page.LoginPage(self.driver)
        value = lp.code_none(vcode)
        assert '登录' == value

    @allure.story("登录模块测试")
    @allure.title("点击我是老板，跳转找工人页面")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_05(self):
        allure.dynamic.description("点击我是老板，跳转找工人页面")
        lp = scr.page.login_page.LoginPage(self.driver)
        value = lp.boss_popup()
        assert '找工人' in value

    @allure.story("登录模块测试")
    @allure.title("点击我是工人，跳转找工作页面")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_06(self):
        allure.dynamic.description("点击我是工人，跳转找工作页面")
        lp = scr.page.login_page.LoginPage(self.driver)
        value = lp.findjob_popup()
        print(value)
        assert '找工作' in value