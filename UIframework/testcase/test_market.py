#-*- coding:utf-8 -*-
from UIframework.page.app import App
from UIframework.page.logger import log_init


class TestMarket:
    def setup(self):
        self.app=App()
       # log_init()

    def test_goto_market(self):
        self.app.start().goto_main().goto_market().goto_search().search()