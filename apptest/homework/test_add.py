#coding:utf-8



import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

def get_datas():
    with open("data.yml",encoding='utf-8') as f:
        all_datas = yaml.safe_load(f)
    return all_datas['datas']

class TestAdd:
    datas = get_datas()
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps['settings[waitForIdleTimeout]'] = 1
        # 客户端与appium 服务器建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()
    @pytest.mark.parametrize("name,phone",datas)
    def test_add(self,name,phone):
        #打开通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()

        #点击添加成员
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        #点击手动输入添加
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/ipb").click()
        #输入姓名
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/b7m").send_keys("name")
        #输入手机号
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/fwi").send_keys("phone")
        #点击保存
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()

