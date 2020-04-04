from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage():
    # driver后面使用了：，方面后面的变量是用. 可以自动弹出对应的方法，注意这里用的是大写的WebDriver
    def __init__(self, driver: WebDriver = None):
        self.driver: webdriver = None
        if driver is None:
            option = webdriver.ChromeOptions()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
            # 这里复用了我已经登录上的企业微信，所有可以直接用get 登录到任何需要登录后的地址
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
            self.driver.implicitly_wait(4)
        else:
            self.driver = driver
