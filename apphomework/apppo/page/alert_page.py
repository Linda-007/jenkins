from appium.webdriver.common.mobileby import MobileBy

from apptest.apppo.page.search_page import SearchContactPage


class AlertPage():
    def alertpage(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text='确定']")
        return SearchContactPage()
