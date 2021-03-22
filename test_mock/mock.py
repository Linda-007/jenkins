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

    def response(self,flow:http.HTTPFlow):
        #判断请求的url是否包含制定的url信息
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            #拿到相应数据信息
            #flow.response.text是str属性，所以如果要操作这个对象的话，必须转换为
            #python字典的数据结构，否则只能使用个str相关的用法

            data = json.loads(flow.response.text)
            data["data"]["items"][0]["quote"]["name"] = "RoseLin"

            percents = [0.0000,-0.1,100000000,1,0.008,500,99999999]
            for item  in range(len(percents)):
                data["data"]["items"][item]["quote"]["percent"]=percents[item]

            flow.response.text = json.dumps(data)
            print(flow.response.text)


#addons是mitmproxy的强制要求规范
#一定要使用此变量名存放类的实例
addons = [
    Counter()
]