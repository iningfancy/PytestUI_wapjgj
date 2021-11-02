'''
-*- coding:utf-8 -*-
@Author:WillowZhang
@Email:116995292@qq.com
@Time:2021/10/20  9:51
'''

import logging
import allure
import pytest
from selenium import webdriver
from scr.common.get_log import get_log

web_driver = None

@pytest.fixture(scope='session', autouse='Ture')
def LoggerGet():
    '''启用日志'''
    get_log()

@pytest.fixture(scope='function', autouse='Ture')
def driver_init(request, browser='chrome'):
    print('--------------open browser--------------')
    global web_driver
    mobileEmulation = {"deviceName": "iPhone X"}
    # Chrome使用手机调试模式显示
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobileEmulation)

    # 适配不同浏览器
    if browser == 'chrome' and web_driver is None:
        web_driver = webdriver.Chrome(options=options)
        # self.driver = webdriver.Chrome()
    elif browser == 'firefox' and web_driver is None:
        web_driver = webdriver.Firefox()
    elif browser == 'ie' and web_driver is None:
        web_driver = webdriver.Ie()
    elif browser == 'edge' and web_driver is None:
        web_driver = webdriver.Edge()
    else:
        logging.error('不支持的浏览器类型:{}'.format(browser))  # 创建error日志
        raise Exception('不支持的浏览器类型:{}'.format(browser))
    request.cls.driver = web_driver
    # 浏览器最大化
    # driver.maximize_window()
    # 隐式等待-一般写10即可
    web_driver.implicitly_wait(10)

    yield web_driver
    print('--------------close browser--------------')
    try:
        web_driver.quit()
        web_driver = None
        logging.info('driver退出成功')  # 创建info日志
    except Exception as e:
        return e
        logging.error(f'driver退出失败,报错信息为{e}')  # 创建error日志

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item,call):
    '''    　　
    每个测试用例执行后，制作测试报告
    　　:param item:测试用例对象
    　　:param call:测试用例的测试步骤
    　　         执行完常规钩子函数返回的report报告有个属性叫report.when
                先执行when=’setup’ 返回setup 的执行结果
                然后执行when=’call’ 返回call 的执行结果
                最后执行when=’teardown’返回teardown 的执行结果
    　　:return:
    '''
    outcome = yield
    report = outcome.get_result() # 获取用例执行后的结果

    if report.when == 'call' and report.failed:
        if report.outcome == 'failed':
            img = web_driver.get_screenshot_as_png()
            with allure.step("添加失败截图："):
                allure.attach(img,"失败截图",allure.attachment_type.PNG)