

from UIframework.page.basepage import BasePage


class Search(BasePage):
    def search(self):
        #输入搜索内容
        # self.find_and_send(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/search_input_text']","alibaba")

        self.parse("../page/search.yaml","search")

