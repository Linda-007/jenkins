# -*- coding: utf-8 -*-


"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
"""
import json

from mitmproxy import ctx, http


class Counter:


    def request(self, flow):
        pass
        # self.num = self.num + 1
        # ctx.log.info("We've seen %d flows" % self.num)
    def request(self,flow):
        """
        使用request时间实现maplocal
        :param flow:
        :return:
        """
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            with open("C:\\Users\\fulinxin\ceshiren实战项目\\test_mock\\map_local.py",encoding="utf-8") as f:
                #给flow.response属性进行赋值，
                #赋值调用mitmproxy响应对象的make方法
                #响应体在make函数里面所需要的数据是str
                flow.response = http.HTTPResponse.make(
                    200,  # (optional) status code
                    f.read() ,  # (optional) content
                    {"Content-Type": "text/html"}  # (optional) headers
                )

    def response(self,flow:http.HTTPFlow):
        pass

#addons是mitmproxy的强制要求规范
#一定要使用此变量名存放类的实例
addons = [
    Counter()
]