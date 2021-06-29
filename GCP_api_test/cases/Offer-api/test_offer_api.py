import allure
import pytest
import os
from common.read_yaml import get_yaml
from common.dingding import send_dingding

# 获取yaml文件数据
yaml_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "offer_api.yaml")
test_data = get_yaml(yaml_file)


@allure.feature("offer_api模块")
class TestOfferApi():

    module = "Offer-api"

    @allure.title("offer-查询接口")
    @pytest.mark.parametrize("test_input, expect", test_data["test_01"])
    def test_01(self, base_url, common_session, test_input, expect):
        '''offer-查询接口'''
        url = base_url + "/offer-api/v1/query"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert res.json()["message"] == expect["message"]
        except:
            send_dingding("offer-查询接口", self.module, api_text)
            assert False


    @allure.title("offer-查询批量接口")
    def test_02(self, base_url, common_session):
        '''offer-查询批量接口'''
        url = base_url + "/offer-api/v1/batch_query"
        data = {
      "ids": [
        "reprehenderit sit tempor",
        "Duis veniam pariatur anim",
        "culpa in "
      ]
    }
        res = common_session.post(url, json = data)
        api_text = res.text
        print(api_text)
        try:
            assert res.json()["code"] == 0
        except:
            send_dingding("offer-查询批量接口", self.module, api_text)
            assert False


    @allure.title("offer查询功能-[API]_v2")
    @pytest.mark.parametrize("test_input, expect", test_data["test_03"])
    def test_03(self, base_url, common_session, test_input, expect):
        '''offer查询功能-[API]_v2'''
        url = base_url + "/offer-api/v2/query"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert res.json()["message"] == expect["message"]
        except:
            send_dingding("offer查询功能-[API]_v2", self.module, api_text)
            assert False