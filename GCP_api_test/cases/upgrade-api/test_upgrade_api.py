from common.read_yaml import get_yaml
import os
import pytest
import allure
from common.dingding import send_dingding

# 获取yaml文件数据
yaml_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "upgrade_api.yaml")
test_data = get_yaml(yaml_file)


@allure.feature("uograde_api模块")
class TestUpgradeApi():

    module = "upgrade-api"

    @allure.title("查询更新配置")
    @pytest.mark.parametrize("test_input, expect", test_data["test_01"])
    def test_01(self, base_url, common_session, test_input, expect):
        '''查询更新配置'''
        url = base_url + "/up/v1/get_config"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
        except:
            send_dingding("查询更新配置", self.module, api_text)
            assert False
