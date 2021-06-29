import pytest
import allure
from common.read_yaml import get_yaml
import os
from common.dingding import send_dingding

# 获取yaml文件数据
yaml_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "pay_api.yaml")
test_data = get_yaml(yaml_file)

@allure.feature("pay_api模块")
class TestPayApi():

    module = "pay-api"

    @allure.title("获取用户余额")
    @pytest.mark.parametrize("test_input, expect", test_data["test_01"])
    def test_01(self, base_url, common_session, test_input, expect):
        '''获取用户余额'''
        url = base_url + "/balance-api/v1/balance"
        res= common_session.get(url, params = test_input)
        api_text = res.text
        print(api_text)
        try:
            assert res.json()["code"] == expect["code"]
            assert type(res.json()["body"]["balance"]) == type(expect["balance"])
        except:
            try:
                assert res.json()["code"] == expect["code"]
                assert expect["message"] in res.json()["message"]
            except:
                send_dingding("获取用户余额", self.module, api_text)
                assert False


    @allure.title("下发银行列表")
    def test_02(self, base_url, common_session):
        '''下发银行列表'''
        url = base_url + "/pay-api/withdraw/banks"
        res = common_session.get(url)
        api_text = res.text
        try:
            assert res.json()["code"] == 0
            assert res.json()["body"]["records"][0]["bankName"] == "Bank Central Asia (BCA)"
        except:
            send_dingding("下发银行列表", self.module, api_text)
            assert False


    @allure.title("获取提现配置")
    def test_03(self, base_url, common_session):
        '''获取提现配置'''
        url = base_url + "/pay-api/withdraw/config"
        res = common_session.get(url)
        api_text = res.text
        try:
            assert res.json()["code"] == 0
            assert res.json()["body"]["withdrawAmount"][0]["name"] == "Rp50.000"
        except:
            send_dingding("获取提现配置", self.module, api_text)
            assert False


    @allure.title("提现操作")
    @pytest.mark.parametrize("test_input, expect", test_data["test_04"])
    def test_04(self, base_url, common_session, test_input, expect):
        '''提现操作'''
        url = base_url + "/pay-api/user/withdraw"
        res = common_session.post(url, data=test_input)
        api_text = res.text
        print(api_text)
        try:
            assert res.json()["code"] == expect["code"]
            assert res.json()["body"]["userBalance"]["userId"] == test_input["__userId"]
        except:
            try:
                assert res.json()["code"] == expect["code"]
                assert res.json()["message"] == expect["message"]
            except:
                send_dingding("提现操作", self.module, api_text)
                assert False


    @allure.title("获取提现历史")
    @pytest.mark.parametrize("test_input, expect", test_data["test_05"])
    def test_05(self, base_url, common_session, test_input, expect):
        '''获取提现历史'''
        url = base_url + "/pay-api/user/withdraw/history"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        print(api_text)
        try:
            assert res.json()["code"] == expect["code"]
            assert type(res.json()["body"]["records"]) == type(expect["records"])
        except:
            try:
                assert res.json()["code"] == expect["code"]
                assert res.json()["message"] == expect["message"]
            except:
                send_dingding("获取提现历史", self.module, api_text)
                assert False


    @allure.title("获取返利历史")
    @pytest.mark.parametrize("test_input, expect", test_data["test_06"])
    def test_06(self, base_url, common_session, test_input, expect):
        '''获取返利历史'''
        url = base_url + "/pay-api/user/cashback/history"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        print(api_text)
        try:
            assert res.json()["code"] == expect["code"]
            assert type(res.json()["body"]["records"]) == type(expect["records"])
        except:
            try:
                assert res.json()["code"] == expect["code"]
                assert res.json()["message"] == expect["message"]
            except:
                send_dingding("获取返现历史", self.module, api_text)
                assert False


    @allure.title("获取在途订单和首页历史订单")
    @pytest.mark.parametrize("test_input, expect", test_data["test_07"])
    def test_07(self, base_url, common_session, test_input, expect):
        '''获取在途订单和首页历史订单'''
        url = base_url + "/pay-api/user/cashback/preparelist"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert type(res.json()["body"]["prepare_total"]) == type(expect["prepare_total"])
        except:
            try:
                assert res.json()["code"] == expect["code"]
                assert res.json()["message"] == expect["message"]
            except:
                send_dingding("获取在途订单和首页历史订单", self.module, api_text)
                assert False


    @allure.title("分页加载历史订单")
    @pytest.mark.parametrize("test_input, expect", test_data["test_08"])
    def test_08(self, base_url, common_session, test_input, expect):
        '''分页加载历史订单'''
        url = base_url + "/pay-api/user/cashback/historylist"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert res.json()["message"] == expect["message"]
        except:
            try:
                assert res.json()["code"] == expect["code"]
            except:
                send_dingding("分页加载历史订单", self.module, api_text)
                assert False


