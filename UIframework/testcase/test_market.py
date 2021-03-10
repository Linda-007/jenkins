#-*- coding:utf-8 -*-
from UIframework.page.app import App


class TestMarket:
    def setup(self):
        self.app=App()
        #self.app.start().goto_main()
    def test_goto_market(self):
        self.app.start().goto_main().goto_market()