from appium.webdriver.common.mobileby import MobileBy

from apptest.apppo.page.base_page import BasePage
from apptest.apppo.page.personhome_page import PersonHomePage


class SearchContactPage(BasePage):
    name = "RT"
    def search_contact(self,name):
        self.find(MobileBy.XPATaH, '//*[@text="鎼滅储"]').send_keys("name")
        elelist = self.find(MobileBy.XPATaH, '//*[@text="RT"]')
        # find_elements 鏂规硶杩斿洖鐨勬槸涓�涓垪琛╗element1,element2...]
        if len(elelist) > 1:
            elelist[1].click()
        else:
            print("鏃犳悳绱㈢粨鏋�")
        return PersonHomePage()

