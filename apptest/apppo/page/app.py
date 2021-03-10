
#鍚姩app,鍋滄app,閲嶅惎app
import yaml
from appium import webdriver

from apptest.apppo.page.base_page import BasePage
from apptest.apppo.page.mian_page import MainPage

with open("../datas/caps.yaml") as f:
    datas = yaml.safe_load(f)
    desires = datas['desirecaps']
    ip = datas['server']['ip']
    port = datas['server']['port']
class App(BasePage):
    def start(self):
        if self.driver == None:

            # 鍚姩app

            # caps['settings[waitForIdleTimeout]'] = 1
            # 瀹㈡埛绔笌appium 鏈嶅姟鍣ㄥ缓绔嬭繛鎺ョ殑浠ｇ爜
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", desires)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        # 閲嶅惎app
        self.driver.close_app()
        self.driver.launch_app()


    def stop(self):
        # 鍋滄app
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)