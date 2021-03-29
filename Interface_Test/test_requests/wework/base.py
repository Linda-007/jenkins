import requests


class Base:
    def __init__(self):
        self.s = requests.Session()
        self.token = self.get_token()
        self.s.params = {"access_token": self.token}

    def get_token(self):
        # proxies = {"https": "http://127.0.0.1:8888"}
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {"corpid": "ww1b0bd60c474de0f9",
                  "corpsecret": "3M4gWSNRrDIe2QE2yaHgJIqc_34auAaHqEyoSq0rX4k"}
        r = self.s.get(url, params=params)  # , proxies=proxies, verify=False
        return r.json()["access_token"]

    def send(self,*args,**kwargs):
        return self.s.request(*args,**kwargs)