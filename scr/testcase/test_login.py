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
    @allure.title("登录测试用例01")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("登录模块")
    @pytest.mark.parametrize('caseinfo',read_excel("./data/data.xlsx","login"))
    def test_login_01(self,caseinfo):
        index,case_name,phone,code,is_exe,result = caseinfo
        #加上用例名称和描述
        allure.dynamic.description(case_name)
        lp = scr.page.login_page.LoginPage(self.driver)
        value = lp.login(phone,code)
        assert '个人中心' == value
        # print(value)

    @allure.story("登录模块测试")
    @allure.title("登录测试用例02")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("登录模块")
    @pytest.mark.parametrize('caseinfo',read_excel("./data/data.xlsx","login_fail"))
    def test_login_02(self,caseinfo):
        index,case_name,phone,code,is_exe,result = caseinfo
        #加上用例名称和描述
        allure.dynamic.description(case_name)
        lp = scr.page.login_page.LoginPage(self.driver)
        value = lp.login_fail(phone,code)
        assert '输入' in value

