from selenium import webdriver
import time
import pytest
from pages.login_page import Loginpage

@pytest.fixture(scope='session')
def driver(request):
    _driver = webdriver.Chrome()
    _driver.maximize_window()      #串口最大化


    def end():
         '''测试完成后，执行终结函数'''
         print('用例完成，5秒后退出')
         time.sleep(5)
         _driver.quit()

    request.addfinalizer(end)
    return _driver
@pytest.fixture(scope='session')
def login(driver):
    '''前置：登陆'''
    web = Loginpage(driver)
    web.login()
    return driver

