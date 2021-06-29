import allure
import pytest
from common.read_yaml import get_yaml
import os
from common.dingding import send_dingding

# 获取yaml文件数据
yaml_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "msg_center_api.yaml")
test_data = get_yaml(yaml_file)


@allure.feature("msg_center_api模块")
class TestMsgCenterApi():

    module = "msg-center-api"

    @allure.title("获取用户消息列表")
    @pytest.mark.parametrize("test_input, expect", test_data["test_01"])
    def test_01(self, base_url, common_session, test_input, expect):
        '''获取用户消息列表'''
        url = base_url + "/msg-center-api/msg/list"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert type(res.json()["body"]["records"]) == type(expect["records"])
        except:
            try:
                assert res.json()["code"] == expect["code"]
                assert res.json()["message"] == expect["message"]
            except:
                send_dingding("获取用户消息列表", self.module, api_text)
                assert False
