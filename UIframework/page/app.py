#-*-coding:utf-8-*-
import yaml
from appium import webdriver

from UIframework.page.basepage import BasePage
from UIframework.page.main_page import MainPage

with open("../datas/caps.yaml") as f:
    datas = yaml.safe_load(f)
    desires = datas['desirecaps']
    ip = datas['server']['ip']
    port = datas['server']['port']
class App(BasePage):
    def start(self):
        if self.driver == None:



            # caps['settings[waitForIdleTimeout]'] = 1
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", desires)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        # 开启app
        self.driver.close_app()
        self.driver.launch_app()


    def stop(self):
        # 关闭app
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)