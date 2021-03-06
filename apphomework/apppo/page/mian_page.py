

from appium.webdriver.common.mobileby import MobileBy



#主页
from appium.webdriver.webdriver import WebDriver

from apptest.apppo.page.addresslist_page import AddressListPage
from apptest.apppo.page.base_page import BasePage
from apptest.apppo.page.search_page import SearchContactPage


class MainPage(BasePage):
    addresslist_element = (MobileBy.XPATH,'//*[@text="通讯录"]')
    def goto_addresslist(self):
        #点击通讯录
        self.find(*self.addresslist_element).click()
        #self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        return AddressListPage(self.driver)

    def goto_searchpage(self):
        #点击搜索框
        self.find_and_click(MobileBy.ID, "com.tencent.wework:id/igk")
        return SearchContactPage(self.driver)
