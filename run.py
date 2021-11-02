'''
-*- coding:utf-8 -*-
@Author:WillowZhang
@Email:116995292@qq.com
@Time:2021/10/18  15:45
'''
import os

import pytest

if __name__ == '__main__':
    pytest.main(['-vs','./scr/testcase/test_login.py'])
    os.system('allure generate ./temp -o ./report --clean')
