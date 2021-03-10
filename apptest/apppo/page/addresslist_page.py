from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from apptest.apppo.page.addcontact_page import AddContactPage
from apptest.apppo.page.base_page import BasePage


class AddressListPage(BasePage):

    def click_addcontact(self):
        elelemt = self.swipe_find("娣诲姞鎴愬憳")
        elelemt.click()
        return AddContactPage(self.driver)
