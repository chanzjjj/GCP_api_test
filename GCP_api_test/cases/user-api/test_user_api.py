import os
from common import db_connect
import pytest
from common.read_yaml import get_yaml
import allure
from common.dingding import send_dingding

# 获取yaml文件数据
yaml_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "user_api.yaml")
test_data = get_yaml(yaml_file)

@allure.feature("user_api模块")
class TestUserApi():

    module = "user-api"

    @allure.title("初始设备id")
    @pytest.mark.parametrize("test_input, expect", test_data["test_01"])
    def test_01(self, base_url, common_session, test_input, expect):
        '''初始设备id'''
        url = base_url + "/user-api/guest/init"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert type(res.json()["body"]["record"]["guestId"]) == type(expect["guestId"])
        except:
            send_dingding("初始设备id", self.module, api_text)
            assert False

    @allure.title("字典地址")
    @pytest.mark.parametrize("test_input, expect", test_data["test_02"])
    def test_02(self, base_url, common_session, test_input, expect):
        '''字典地址'''
        url = base_url + "/user-api/address/get"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert type(res.json()["BALI"]["KAB. BADUNG"]["ABIANSEMAL"]) == type(expect["ABIANSEMAL"])
        except:
            send_dingding("字典地址", self.module, api_text)
            assert False

    @allure.title("提交反馈")
    @pytest.mark.parametrize("test_input_data, test_input_body, expect", test_data["test_03"])
    def test_03(self, base_url, common_session, test_input_data, test_input_body, expect):
        '''提交反馈'''
        url = base_url + "/user-api/feedback"
        head = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        common_session.headers.update(head)
        res = common_session.post(url, params = test_input_data, data = test_input_body)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
        except:
            send_dingding("提交反馈", self.module, api_text)
            assert False

    @allure.title("第三方登录")
    @pytest.mark.parametrize("test_input, expect", test_data["test_04"])
    def test_04(self, base_url, common_session, test_input, expect):
        '''第三方登录'''
        url = base_url + "/user-api/user/thirdLogin/facebook"
        res = common_session.post(url, data = test_input)
        api_text = res.text
        # print(res.text)
        try:
            assert res.json()["code"] == expect["code"]
            assert type(res.json()["body"]["userInfo"]["userId"]) == type(expect["userId"])
        except:
            try:
                assert res.json()["code"] == expect["code"]
                assert res.json()["message"] == expect["message"]
            except:
                send_dingding("第三方登录", self.module, api_text)
                assert False

    @allure.title("申请卡")
    @pytest.mark.parametrize("test_input, expect", test_data["test_05"])
    def test_05(self, base_url, common_session, test_input, expect):
        '''申请卡'''
        url = base_url + "/user-api/vipcard/apply"
        res = common_session.post(url, params = test_input)
        api_text = res.text
        print(type(api_text))
        try:
            assert res.json()["code"] == expect["code"]
            assert res.json()["message"] == expect["message"]
        except:
            try:
                assert res.json()["code"] == expect["code"]
            except AssertionError:
                send_dingding("申请卡", "user-api", api_text)
                assert False



    @allure.title("激活卡'")
    @pytest.mark.parametrize("test_input, expect", test_data["test_06"])
    def test_06(self, base_url,common_session, test_input, expect):
        '''激活卡'''
        url = base_url + "/user-api/vipcard/active/v2"
        res = common_session.post(url, data = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert res.json()["message"] == expect["message"]
        except:
            send_dingding("激活卡", self.module, api_text)
            assert False


    @allure.title("邮费下发")
    def test_07(self, base_url, common_session):
        '''邮费下发'''
        url = base_url + "/user-api/vipcard/postage"
        res = common_session.get(url)
        api_text = res.text
        try:
            assert res.json()["code"] == 0
        except:
            send_dingding("邮费下发", self.module, api_text)
            assert False

    @allure.title("添加心愿单")
    @pytest.mark.parametrize("test_input, expect", test_data["test_08"])
    def test_08(self, base_url, common_session, test_input, expect):
        '''添加心愿单'''
        url = base_url + "/user-api/wishlist/add"
        db_connect.delete_wish_list(user_id = test_input["__userId"], product_id = test_input["productId"])
        res = common_session.get(url, params = test_input)
        api_text = res.text
        print(api_text)
        try:
            assert res.json()["code"] == expect["code"]
            assert res.json()["message"] == expect["message"]
        except:
            try:
                assert res.json()["code"] == expect["code"]
            except:
                send_dingding("添加心愿单", self.module, api_text)
                assert False

    @allure.title("心愿单列表")
    @pytest.mark.parametrize("test_input, expect", test_data["test_09"])
    def test_09(self, base_url, common_session, test_input, expect):
        '''心愿单列表'''
        url = base_url + "/user-api/wishlist/get"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert type(res.json()["body"]["total"]) == type(expect["total"])
        except:
            send_dingding("心愿单列表", self.module, api_text)
            assert False

    @allure.title("删除心愿单")
    @pytest.mark.parametrize("test_input, expect", test_data["test_10"])
    def test_10(self, base_url, common_session, test_input, expect):
        '''删除心愿单'''
        url = base_url + "/user-api/wishlist/remove"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        print(api_text)
        try:
            assert res.json()["code"] == expect["code"]
            assert res.json()["message"] == expect["message"]
        except:
            try:
                assert res.json()["code"] == expect["code"]
            except:
                send_dingding("删除心愿单", self.module, api_text)
                assert False

    @allure.title("判断是否已添加心愿单")
    @pytest.mark.parametrize("test_input, expect", test_data["test_11"])
    def test_11(self, base_url, common_session, test_input, expect):
        '''判断是否已添加心愿单'''
        url = base_url + "/user-api/wishlist/checkWished"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        print(api_text)
        try:
            assert res.json()["code"] == expect["code"]
            assert type(res.json()["body"]["isWished"]) == type(expect["isWished"])
        except:
            try:
                assert res.json()["code"] == expect["code"]
                assert res.json()["message"] == expect["message"]
            except:
                send_dingding("判断是否已添加心愿单", self.module, api_text)
                assert False


    @allure.title("获取用户主信息")
    @pytest.mark.parametrize("test_input, expect", test_data["test_12"])
    def test_12(self, base_url, common_session, test_input, expect):
        '''获取用户主信息'''
        url = base_url + "/user-api/user/info/v2"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert res.json()["message"] == expect["message"]
        except:
            try:
                assert res.json()["code"] == expect["code"]
                assert res.json()["body"]["userInfo"]["userId"] == test_input["__userId"]
            except:
                send_dingding("获取用户主信息", self.module, api_text)
                assert False


    @allure.title("更新用户信息")
    @pytest.mark.parametrize("test_input, expect", test_data["test_13"])
    def test_13(self, base_url, common_session, test_input, expect):
        '''更新用户信息'''
        url = base_url + "/user-api/user/update"
        res = common_session.post(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert res.json()["message"] == expect["message"]
        except:
            try:
                assert res.json()["code"] == expect["code"]
                assert res.json()["body"]["userInfo"]["userId"] == test_input["__userId"]
            except:
                send_dingding("更新用户信息", self.module, api_text)
                assert False
