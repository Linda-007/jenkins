from appium.webdriver.common.mobileby import MobileBy

from apptest.apppo.page.base_page import BasePage


class EditContactPage(BasePage):
    def edit_contact(self,name,phonenumber):
        self.find(MobileBy.XPATH, '//*[contains(@text,"姓名")]/../*[@text="必填"]').send_keys(name)
        self.find(MobileBy.XPATH, '//*[contains(@text,"手机")]/..//*[@text="必填"]').send_keys(phonenumber)
        self.find_and_click(MobileBy.XPATH, '//*[@text="保存"]')
        # 验证toast

    def verify_ok(self):
        self.find(MobileBy.XPATH,'//*[@text="添加成功"]')

