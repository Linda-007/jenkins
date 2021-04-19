from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException


class TestContact:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        #跳过uiautomator2server的安装等服务
        caps['skipServerInstallation'] = 'true'
        #跳过设备初始化
        caps['skipDeviceInitialization'] = 'true'
        #启动之前不停止app
        caps['dontStopAppOnReset'] = 'true'

        #caps['settings[waitForIdleTimeout]'] = 1
        # 客户端与appium 服务器建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def swipe_find(self,text,num=3):
        for i in range(num):
            if i == num-1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找到{num}次，未找到")

            self.driver.implicitly_wait(1)
            try:
                element = self.driver.find_element(MobileBy.XPATH, f'//*[@text="{text}"]').click()
                self.driver.implicitly_wait(5)
                return element
            except:
                print("未找到")
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get('height')

                start_x = width/2
                start_y = height*0.8

                end_x = start_x
                end_y = height*0.3

                self.driver.swipe(start_x,start_y,end_x,end_y,1000)

            #return element

    def test_contact(self):
        name = "Linda"
        phonenumber = "13567899876"
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        #self.driver.find_element(MobileBy.XPATH,'//*[@text="添加成员"]').click()
        elelemt = self.swipe_find("添加成员")
        elelemt.click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"姓名")]/../*[@text="必填"]').send_keys(name)
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"手机")]/..//*[@text="必填"]').send_keys(phonenumber)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
        #验证toast
        sleep(3)
        print(self.driver.page_source)

        # assert "添加成功" in self.driver.page_source
        self.driver.find_element(MobileBy.XPATH,'//*[@text="添加成功"]')
    def test_delcontact(self):
        name = "姐姐"
        self.driver.find_element(MobileBy.XPATaH,'//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/igk").click()
        self.driver.find_element(MobileBy.XPATaH,'//*[@text="搜索"]').send_keys("name")
        elelist = self.driver.find_elements(MobileBy.XPATaH,'//*[@text="姐姐"]')
        #find_elements 方法返回的是一个列表[element1,element2...]
        if len(elelist)>1:
            elelist[1].click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/iga").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='编辑成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='删除成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
