import allure
import pytest
from common.read_yaml import get_yaml
import os
from common.dingding import send_dingding

# 获取yaml文件数据
yaml_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "activity_api.yaml")
test_data = get_yaml(yaml_file)


@allure.feature("activity_api模块")
class TestActivityApi():

    module = "activity-api"

    @allure.title("查询当前活动id")
    @pytest.mark.parametrize("test_input, expect", test_data["test_01"])
    def test_01(self, base_url, common_session, test_input, expect):
        '''查询当前活动id'''
        url = base_url + "/activity-api/v1/current"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert type(res.json()["data"]["activity_id"]) == type(expect["activity_id"])
        except:
            try:
                assert res.json()["code"] == expect["code"]
                assert res.json()["message"] == expect["message"]
            except:
                send_dingding("查询当前活动id", self.module, api_text)
                assert False


    @allure.title("查询最近邀请记录列表")
    @pytest.mark.parametrize("test_input, expect", test_data["test_02"])
    def test_02(self, base_url, common_session, test_input, expect):
        '''查询最近邀请记录列表'''
        url = base_url + "/activity-api/v1/fission/recent_invite_list"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert type(res.json()["data"]["records"]) == type(expect["records"])
        except:
            try:
                assert res.json()["code"] == expect["code"]
                assert res.json()["message"] == expect["message"]
            except:
                send_dingding("查询最近邀请记录列表", self.module, api_text)
                assert False


    @allure.title("查询活动详情")
    @pytest.mark.parametrize("test_input, expect", test_data["test_03"])
    def test_03(self, base_url, common_session, test_input, expect):
        '''查询活动详情'''
        url = base_url + "/activity-api/v1/query"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert res.json()["data"]["activity_id"] == test_input["activity_id"]
        except:
            try:
                assert res.json()["code"] == expect["code"]
                assert res.json()["message"] == expect["message"]
            except:
                send_dingding("查询活动详情", self.module, api_text)
                assert False


    @allure.title("查询邀请码")
    @pytest.mark.parametrize("test_input, expect", test_data["test_04"])
    def test_04(self, base_url, common_session, test_input, expect):
        '''查询邀请码'''
        url = base_url + "/activity-api/v1/fission/query_referral_code"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert type(res.json()["data"]["referral_code"]) == type(expect["referral_code"])
        except:
            try:
                assert res.json()["code"] == expect["code"]
                assert res.json()["message"] == expect["message"]
            except:
                send_dingding("查询邀请码", self.module, api_text)
                assert False


    @allure.title("邀请记录查询")
    @pytest.mark.parametrize("test_input, expect", test_data["test_05"])
    def test_05(self, base_url, common_session, test_input, expect):
        '''邀请记录查询'''
        url = base_url + "/activity-api/v1/fission/query_invite_record"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert type(res.json()["data"]["records"]) == type(expect["records"])
        except:
            try:
                assert res.json()["code"] == expect["code"]
                assert res.json()["message"] == expect["message"]
            except:
                send_dingding("邀请记录查询", self.module, api_text)
                assert False


    @allure.title("奖励返现记录查询")
    @pytest.mark.parametrize("test_input, expect", test_data["test_06"])
    def test_06(self, base_url, common_session, test_input, expect):
        '''奖励返现记录查询'''
        url = base_url + "/activity-api/v1/fission/query_reward_record"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert res.json()["message"] == expect["message"]
        except:
            send_dingding("奖励返现记录查询", self.module, api_text)
            assert False


    @allure.title("启动最近邀请记录机器人")
    def test_07(self, base_url, common_session):
        '''启动最近邀请记录机器人'''
        url = base_url + "/activity-api/v1/fission/start_rb"
        res = common_session.get(url)
        api_text = res.text
        try:
            assert res.json()["code"] == 0
        except:
            send_dingding("启动最近邀请记录机器人", self.module, api_text)
            assert False


    @allure.title("停止最近邀请记录机器人")
    def test_08(self, base_url, common_session):
        '''停止最近邀请记录机器人'''
        url = base_url + "/activity-api/v1/fission/stop_rb"
        res = common_session.get(url)
        api_text = res.text
        try:
            assert res.json()["code"] == 0
        except:
            send_dingding("停止最近邀请记录机器人", self.module, api_text)
            assert False