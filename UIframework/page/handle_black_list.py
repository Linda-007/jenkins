import allure
from appium.webdriver.common.mobileby import MobileBy

from UIframework.page.logger import log


def handle_black(func):
    def run(*args,**kwargs):
        # 弹框出现后，进行处理，
        black_list = ["//*[@resource-id='com.xueqiu.android:id/iv_close']"]
        #相当于self
        instance = args[0]
        #args = args[]
        try:
            log.debug("find" + args[2])
            return func(*args,**kwargs)
        except Exception:
            # instance.screenshot()
            # with open("./tmp.png","rb") as f:
            #     allure.attach(f.read(),attachment_type=allure.attachment_type.PNG)

            allure.attach(instance.screenshot(), attachment_type=allure.attachment_type.PNG)

            # 捕获异常(自动化时出现的各种弹窗)
            for ele_xpath in black_list:
                # 查看异常是否存在
                eles = instance.finds(MobileBy.XPATH, ele_xpath)
                # 存在异常就杀掉
                if len(eles) > 0:
                    eles[0].click()
                    return func(*args,**kwargs)
    return run
