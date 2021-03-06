from appium.webdriver.common.mobileby import MobileBy

from apptest.apppo.page.base_page import BasePage
from apptest.apppo.page.personinfo_page import PersonInfoPage


class PersonHomePage(BasePage):
    def click_personhome(self):
        #点击个人主页右侧三个小圆点
        self.find_and_click(MobileBy.ID, "com.tencent.wework:id/iga")

        return PersonInfoPage()