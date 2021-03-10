

#娣诲姞鎴愬憳椤�
from appium.webdriver.common.mobileby import MobileBy

from apptest.apppo.page.base_page import BasePage
from apptest.apppo.page.editcontact_page import EditContactPage


class AddContactPage(BasePage):
    def addcontact_menual(self):
        #鎵嬪姩杈撳叆娣诲姞
        self.find(MobileBy.XPATH,'//*[@text="鎵嬪姩杈撳叆娣诲姞"]').click()
        return EditContactPage(self.driver)