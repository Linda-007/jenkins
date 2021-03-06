from appium.webdriver.common.mobileby import MobileBy

from apptest.apppo.page.base_page import BasePage
from apptest.apppo.page.personhome_page import PersonHomePage


class SearchContactPage(BasePage):
    name = "RT"
    def search_contact(self,name):
        self.find(MobileBy.XPATaH, '//*[@text="搜索"]').send_keys("name")
        elelist = self.find(MobileBy.XPATaH, '//*[@text="RT"]')
        # find_elements 方法返回的是一个列表[element1,element2...]
        if len(elelist) > 1:
            elelist[1].click()
        else:
            print("无搜索结果")
        return PersonHomePage()

