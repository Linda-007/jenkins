from appium.webdriver.common.mobileby import MobileBy

from apptest.apppo.page.alert_page import AlertPage
from apptest.apppo.page.base_page import BasePage


class EditPersonPage(BasePage):
    #点击删除成员
    def del_person(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text='删除成员']")
        return AlertPage()