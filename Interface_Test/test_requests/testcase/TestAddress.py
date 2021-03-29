import pytest

from test_requests.wework.wework_address import WeworkAddress


class TestAddress:
    name = "GG"
    user_id = "gg001"
    def setup_class(self):
        self.address  =  WeworkAddress()
        self.mobile = "19923456789"
        self.department = [1,2]

    def setup(self):
        #数据库
        self.user_id += "tmp"
        self.address.delete(self.user_id )

    def teardown(self):
        self.address.delete(self.user_id )

    def test_get_information(self):
        #数据处理
        self.address.create_member(self.user_id,self.name,self.mobile,self.department )

        #用户信息是否正确
        r = self.address.get_information(self.user_id)
        assert r["name"] == self.name

    def test_create_member(self):

        r = self.address.create_member(self.user_id,self.name,self.mobile,self.department)
        assert r.get("errmsg") == "created"
        #断言
        info = self.address.get_information(self.user_id)
        assert info["name"] == self.name

        #数据恢复
        #self.address.delete()
    @pytest.mark.parametrize("user_id,new_name",[("tmp",name+"tmp")]*5)
    def test_update_member(self,user_id,new_name):
        user_id += self.user_id
        self.address.create_member(user_id,self.name,self.mobile,self.department)
        #new_name = self.name + "tmp"
        r = self.address.update(user_id,new_name)
        assert r.get("errmsg") == "updated"
        # 断言
        info = self.address.get_information(user_id)
        assert info["name"] == new_name

    def test_delete_member(self):
        self.address.create_member(self.user_id,self.name,self.mobile,self.department)
        r = self.address.delete(self.user_id)
        assert r.get("errmsg") == "deleted"
        # 断言
        info = self.address.get_information(self.user_id)
        assert info["errcode"] == 60111