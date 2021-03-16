import yaml
from appium.webdriver.common.mobileby import MobileBy

from UIframework.page.basepage import BasePage
from UIframework.page.search import Search


class Market(BasePage):
    def goto_search(self):
        # 点击搜索，进入搜索页面
        # self.find_and_click(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']")

        self.parse("../page/market.yaml", "goto_search")
        return Search(self.driver)