#-*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from UIframework.page.basepage import BasePage


class MainPage(BasePage):
    def goto_market(self):
        #点击页面蓝色的笔，让弹窗出现
        self.find_and_click(MobileBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/post_status"]')
        #点击行情
        self.find_and_click(MobileBy.XPATH,"//*[@text='行情']")
        #点击搜索，进入搜索页面
        self.find_and_click(MobileBy.ID,"com.xueqiu.android:id/action_search")
        #输入搜索内容
        self.find_and_send(MobileBy.ID,"com.xueqiu.android:id/search_input_text","alibaba")