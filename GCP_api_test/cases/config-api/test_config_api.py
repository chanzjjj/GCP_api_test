import allure
import pytest
from common.read_yaml import get_yaml
import os
from common.dingding import send_dingding

# 获取yaml文件数据
yaml_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "config_api.yaml")
test_data = get_yaml(yaml_file)


@allure.feature("config_api模块")
class TestConfigApi():

    module = "config-api"

    @allure.title("客户端配置下发")
    @pytest.mark.parametrize("test_input, expect", test_data["test_01"])
    def test_01(self, base_url, common_session, test_input, expect):
        '''客户端配置下发'''
        url = base_url + "/config-api/config"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert type(res.json()["body"]["configs"]) == type(expect["configs"])
        except:
            send_dingding("客户端配置下发", self.module, api_text)
            assert False