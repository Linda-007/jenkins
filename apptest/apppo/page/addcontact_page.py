

#添加成员页
from appium.webdriver.common.mobileby import MobileBy

from apptest.apppo.page.base_page import BasePage
from apptest.apppo.page.editcontact_page import EditContactPage


class AddContactPage(BasePage):
    def addcontact_menual(self):
        #手动输入添加
        self.find(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        return EditContactPage(self.driver)