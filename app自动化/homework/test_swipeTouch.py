
# 定义加滑动边查找的方法
import pytest
from appium.webdriver import webdriver


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
    self.driver.implicitly_wait(5)


def teardown(self):
    self.driver.quit()

def swipe_find(driver, element, location):
    # 获取滑动的元素坐标点
    lc = element.location
    # 获取滑动元素的大小
    size = element.size
    # 初始化元素坐标点的值
    x = lc['x']
    y = lc['y']
    w = size['width']
    h = size['height']
    startx = x + w * 0.9
    starty = y + h/2
    endx = x + w * 0.1
    while True:
        page = driver.page_source   # 获取的是整个app页面的信息
        try:
            driver.find_element(*location).click()  # 点击对应的频道信息
            return True
        except Exception as e:
            driver.swipe(startx, starty, endx, starty, duration=2000)
        if driver.page_source == page:
            print("已经滑动到最后页面，没有找到对应的频道信息!")
            return False
if __name__ == '__main__':
    pytest.main()