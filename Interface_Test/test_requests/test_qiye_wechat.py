import json

import requests


class TestAddress:
    def setup(self):
        self.token = self.get_token()

    def get_token(self):
        proxies = {"https":"http://127.0.0.1:8888"}
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww1b0bd60c474de0f9&corpsecret=3M4gWSNRrDIe2QE2yaHgJIqc_34auAaHqEyoSq0rX4k"
        r = requests.get(url,proxies=proxies,verify=False)
        return r.json()['access_token']

    def test_get_information(self):
        user_id = 'dg'
        r_info = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={user_id}")
        print(r_info.json())

    def test_create_member(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        data = {
            "userid": "RoseLin110",
            "name": "RoseLin",
            "mobile": "+86 18990908980",
            "department": [1,2],
        }
        r_member = requests.post(url,json.dumps(data))
        print(r_member.json())

    def test_update(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        data = {
            "userid": "aa",
            "name": "Key酱"
        }
        r_update = requests.post(url, json=data)
        print(r_update.json())

    def test_delete(self):
        user_id = 'we'
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={user_id}"
        r_delete = requests.post(url, user_id)
        print(r_delete.json())