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
        url = flow.request.pretty_url
        method = flow.request.method
        with open("template.txt") as f:
            # 拿到文本字符串数据
            data = f.read()
            new_data = data.format(method=method, url=url)
            #将替换好的数据信息写入模板文件
            with open("template.py", "w", encoding="utf-8") as f:
                f.write(new_data)
    def response(self,flow:http.HTTPFlow):
        pass

#addons是mitmproxy的强制要求规范
#一定要使用此变量名存放类的实例
addons = [
    Counter()
]