'''
-*- coding:utf-8 -*-
@Author:WillowZhang
@Email:116995292@qq.com
@Time:2021/10/20  9:51
'''

import logging
import pytest
from selenium import webdriver
from scr.common.get_log import get_log


@pytest.fixture(scope='session',autouse='Ture')
def LoggerGet():
    '''启用日志'''
    get_log()


@pytest.fixture(scope='function',autouse='Ture')

def driver_init(request,browser='chrome'):
    print('--------------open browser--------------')
    mobileEmulation = {"deviceName": "iPhone X"}
    # Chrome使用手机调试模式显示
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation',mobileEmulation)

    # 适配不同浏览器
    if browser == 'chrome':
        web_driver = webdriver.Chrome(options=options)
        # self.driver = webdriver.Chrome()
    elif browser == 'firefox':
        web_driver = webdriver.Firefox()
    elif browser == 'ie':
        web_driver = webdriver.Ie()
    elif browser == 'edge':
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
        logging.info('driver退出成功')  # 创建info日志
    except Exception as e:
        return e
        logging.error(f'driver退出失败,报错信息为{e}')  # 创建error日志