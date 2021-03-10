from appium.webdriver.common.mobileby import MobileBy

from apptest.apppo.page.base_page import BasePage


class EditContactPage(BasePage):
    def edit_contact(self,name,phonenumber):
        self.find(MobileBy.XPATH, '//*[contains(@text,"濮撳悕")]/../*[@text="蹇呭～"]').send_keys(name)
        self.find(MobileBy.XPATH, '//*[contains(@text,"鎵嬫満")]/..//*[@text="蹇呭～"]').send_keys(phonenumber)
        self.find_and_click(MobileBy.XPATH, '//*[@text="淇濆瓨"]')
        # 楠岃瘉toast

    def verify_ok(self):
        self.find(MobileBy.XPATH,'//*[@text="娣诲姞鎴愬姛"]')

