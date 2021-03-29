import json

import requests

from test_requests.wework.base import Base


class  WeworkAddress(Base):
    def get_information(self,user_id:str):
        """
        获取用户信息
        :param user_id:
        :return:
        """
        #user_id = 'dg001'

        params = {"userid":user_id}
        r_info = self.send("GET",
            f"https://qyapi.weixin.qq.com/cgi-bin/user/get",params=params)
        return r_info.json()

    def create_member(self,user_id: str , name: str, mobile: str, department: list):
        """
        创建成员
        :param name:
        :param mobile: 手机号 11位
        :param department: 部门
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        data = {
            "userid": user_id,
            "name": name,
            "mobile": mobile,
            "department": department,
        }
        r_member = self.send("POST",url, json.dumps(data))
        return r_member.json()

    def update(self,user_id,name: str):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        data = {
            "userid": user_id,
            "name": name
        }
        r_update = self.send("POST",url, json=data)
        return r_update.json()

    def delete(self,user_id):
        #user_id = 'dg001'
        params = {"userid":user_id }
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        r_delete = self.send("POST",url, params=params)
        return r_delete.json()