#-*- coding:utf-8 -*-
import yaml
from appium.webdriver.common.mobileby import MobileBy

from UIframework.page.basepage import BasePage
from UIframework.page.market import Market


class MainPage(BasePage):
    def goto_market(self):
        #点击页面蓝色的笔，让弹窗出现
        # self.find_and_click(MobileBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/post_status"]')
        # #点击行情
        # self.find_and_click(MobileBy.XPATH,"//*[@text='行情']")

        self.parse("../page/main_page.yaml","goto_market")

        return Market(self.driver)
