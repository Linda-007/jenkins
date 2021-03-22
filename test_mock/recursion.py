# -*- coding: utf-8 -*-
import json

from mitmproxy import http


class Counter:


    def request(self, flow):
        pass
        # self.num = self.num + 1
        # ctx.log.info("We've seen %d flows" % self.num)

    def response(self,flow:http.HTTPFlow):
        #判断请求的url是否包含制定的url信息
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            #拿到相应数据信息
            #flow.response.text是str属性，所以如果要操作这个对象的话，必须转换为
            #python字典的数据结构，否则只能使用个str相关的用法
            #递归解析响应数据，并对不同的数据类型做不同的处理
            data = self.handle_data(json.loads(flow.response.text))
            #data["data"]["items"][0]["quote"]["name"] = "RoseLin"
            flow.response.text = json.dumps(data)


    def handle_data(self,data):

        """
        递归算法：如果是list就继续遍历列表中的元素
        如果是dict,就继续遍历对应的value
        如果是整型或者float,做倍增
        如果是str,做+ ”a"操作
        """
        #1.罗列各种情况2.针对不同的数据结构做不同的数据处理
        if isinstance(data,dict):
            #如果是dict,就继续遍历对应的value
            for key,value in data.items():
                data[key] =self.handle_data(value)

        elif isinstance(data,list):
            #如果是list就继续遍历列表中的元素
            # data_new = []
            # for item in data:
            #     data_new.append(handle_data(item))
            #把原本遍历操作使用列表推导式表达出来
            data = [self.handle_data(item) for item in data ]

        elif isinstance(data,str):
            #如果是str,做+ ”a"操作
            data = data+"a"
        elif isinstance(data,bool):
            data = data

        elif isinstance(data,(int,float)):
            #如果是整型或者float,做倍增
            data =data*2
        else:
            #如果是其他数据类型，保持原样
            data = data
        return data

addons = [
    Counter()
]

