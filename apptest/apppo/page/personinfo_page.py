from appium.webdriver.common.mobileby import MobileBy

from apptest.apppo.page.base_page import BasePage
from apptest.apppo.page.editperson_page import EditPersonPage


class PersonInfoPage(BasePage):
    def edit_person(self):
        #鐐瑰嚮缂栬緫鎴愬憳
        self.find_and_click(MobileBy.XPATH, "//*[@text='缂栬緫鎴愬憳']")

        return  EditPersonPage()