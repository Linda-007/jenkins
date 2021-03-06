from appium.webdriver.common.mobileby import MobileBy

from apptest.apppo.page.base_page import BasePage
from apptest.apppo.page.editperson_page import EditPersonPage


class PersonInfoPage(BasePage):
    def edit_person(self):
        #点击编辑成员
        self.find_and_click(MobileBy.XPATH, "//*[@text='编辑成员']")

        return  EditPersonPage()