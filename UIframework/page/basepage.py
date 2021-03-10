#-*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def decorator(func):
        def dec(self, *args, **kwargs):

            # 弹框出现后，进行处理，
            black_list = ["//*[@resource-id='com.xueqiu.android:id/iv_close']"]
            try:
                return func(*args, **kwargs)
            except Exception:
                # 捕获异常(自动化时出现的各种弹窗)
                for ele_xpath in black_list:
                    # 查看异常是否存在
                    eles = self.finds(MobileBy.XPATH, ele_xpath)
                    # 存在异常就杀掉
                    if len(eles) > 0:
                        eles[0].click()
                        return dec(*args, **kwargs)

        return dec

    @decorator
    def find(self, locator, value):
        # 弹框出现后，进行处理，
        black_list=["//*[@resource-id='com.xueqiu.android:id/iv_close']"]
        try:
            return self.driver.find_element(locator, value)
        except Exception:
            #捕获异常(自动化时出现的各种弹窗)
            for ele_xpath in black_list:
                #查看异常是否存在
                eles = self.finds(MobileBy.XPATH,ele_xpath)
                #存在异常就杀掉
                if len(eles)>0:
                    eles[0].click()
                    return self.find(locator,value)

    def finds(self, locator, value):

        return self.driver.find_elements(locator, value)

    def find_and_click(self, locator, value):

        self.find(locator, value).click()

    def find_and_send(self, locator, value,content):
        self.find(locator,value).send_keys(content)

    def swipe_find(self, text, num=3):
        for i in range(num):
            if i == num - 1:
                self.driver.implicitly_wait(5)

                raise NoSuchElementException(f"找到{num}次，未找到")

            self.driver.implicitly_wait(1)
            try:
                element = self.driver.find_element(MobileBy.XPATH, f'//*[@text="{text}"]').click()
                self.driver.implicitly_wait(5)
                return element
            except:
                print("未找到")
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get('height')

                start_x = width / 2
                start_y = height * 0.8

                end_x = start_x
                end_y = height * 0.3

                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)
