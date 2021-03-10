

from appium.webdriver.common.mobileby import MobileBy



#涓婚〉
from appium.webdriver.webdriver import WebDriver

from apptest.apppo.page.addresslist_page import AddressListPage
from apptest.apppo.page.base_page import BasePage
from apptest.apppo.page.search_page import SearchContactPage


class MainPage(BasePage):
    addresslist_element = (MobileBy.XPATH,'//*[@text="閫氳褰�"]')
    def goto_addresslist(self):
        #鐐瑰嚮閫氳褰�
        self.find(*self.addresslist_element).click()
        #self.driver.find_element(MobileBy.XPATH,'//*[@text="閫氳褰�"]').click()
        return AddressListPage(self.driver)

    def goto_searchpage(self):
        #鐐瑰嚮鎼滅储妗�
        self.find_and_click(MobileBy.ID, "com.tencent.wework:id/igk")
        return SearchContactPage(self.driver)
