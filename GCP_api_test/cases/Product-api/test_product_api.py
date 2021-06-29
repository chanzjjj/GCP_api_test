import allure
import pytest
import os
from common.read_yaml import get_yaml
from common.dingding import send_dingding

# 获取yaml文件数据
yaml_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "product_api.yaml")
test_data = get_yaml(yaml_file)

@allure.feature("product_api模块")
class TestProductApi():

    module = "product-api"

    @allure.title("商品搜索")
    @pytest.mark.parametrize("test_input, expect", test_data["test_01"])
    def test_01(self, base_url, common_session, test_input, expect):
        '''商品搜索'''
        url = base_url + "/product-api/search/products"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        print(api_text)
        try:
            assert res.json()["code"] == expect["code"]
            assert res.json()["sv"] == expect["sv"]
        except:
            try:
                assert res.json()["code"] == expect["code"]
                assert res.json()["message"] == expect["message"]
            except:
                send_dingding("商品搜索", self.module, api_text)
                assert False


    @allure.title("商品详情")
    @pytest.mark.parametrize("test_input, expect", test_data["test_02"])
    def test_02(self, base_url, common_session, test_input, expect):
        '''商品详情'''
        url = base_url + "/product-api/product/" + test_input["productId"]
        res = common_session.get(url)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert res.json()["body"]["record"]["productId"] == expect["productId"]
        except:
            send_dingding("商品详情", self.module, api_text)


    @allure.title("热词搜索")
    def test_03(self, base_url, common_session):
        '''热词搜索'''
        url = base_url + "/product-api/search/hotSearch"
        res = common_session.get(url)
        api_text = res.text
        try:
            assert res.json()["code"] == 0
            assert type(res.json()["body"]["records"]) == list
        except:
            send_dingding("热词搜索", self.module, api_text)
            assert False


    @allure.title("商品分类列表")
    @pytest.mark.parametrize("test_input, expect", test_data["test_04"])
    def test_04(self, base_url, common_session, test_input, expect):
        '''商品分类列表'''
        url = base_url + "/product-api/search/hotSearch"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert type(res.json()["body"]["records"]) == type(expect["records"])
        except:
            send_dingding("商品分类列表", self.module, api_text)
            assert False


    @allure.title("商品分类-商品列表")
    @pytest.mark.parametrize("test_input, expect", test_data["test_05"])
    def test_05(self, base_url, common_session, test_input, expect):
        '''商品分类-商品列表'''
        url = base_url + "/product-api/categoryProducts/59"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        print(api_text)
        try:
            assert res.json()["code"] == expect["code"]
            assert res.json()["sv"] == expect["sv"]
        except:
            try:
                assert res.json()["code"] == expect["code"]
                assert expect["message"] in res.json()["message"]
            except:
                send_dingding("商品分类-商品列表", self.module, api_text)
                assert False


    @allure.title("商品首页板块")
    @pytest.mark.parametrize("test_input, expect", test_data["test_06"])
    def test_06(self, base_url, common_session, test_input, expect):
        '''商品首页板块'''
        url = base_url + "/product-api/module/home"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert res.json()["sv"] == expect["sv"]
        except:
            send_dingding("商品首页板块", self.module, api_text)
            assert False


    @allure.title("板块商品列表")
    @pytest.mark.parametrize("test_input, expect", test_data["test_07"])
    def test_07(self, base_url, common_session, test_input, expect):
        '''板块商品列表'''
        url = base_url + "/product-api/moduleProducts/2"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert res.json()["sv"] == expect["sv"]
        except:
            try:
                assert res.json()["code"] == expect["code"]
                assert expect["message"] in res.json()["message"]
            except:
                send_dingding("板块商品列表", self.module, api_text)
                assert False


    @allure.title("商品详情v2")
    @pytest.mark.parametrize("test_input, expect", test_data["test_08"])
    def test_08(self, base_url, common_session, test_input, expect):
        '''商品详情v2'''
        url = base_url + "/product-api/product/500001/v2"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert res.json()["sv"] == expect["sv"]
        except:
            send_dingding("商品详情v2", self.module, api_text)
            assert False


    @allure.title("特权-供应商列表v2")
    @pytest.mark.parametrize("test_input, expect", test_data["test_09"])
    def test_09(self, base_url, common_session, test_input, expect):
        '''特权-供应商列表v2'''
        url = base_url + "/product-api/vipPrivilege/offer/list/v2"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert res.json()["sv"] == expect["sv"]
        except:
            try:
                assert res.json()["code"] == expect["code"]
                assert expect["message"] in res.json()["message"]
            except:
                send_dingding("特权-供应商列表v2", self.module, api_text)
                assert False


    @allure.title("特权详情")
    def test_10(self, base_url, common_session):
        '''特权详情'''
        url = base_url + "/product-api/vipPrivilege/detail/143"
        res = common_session.get(url)
        api_text = res.text
        try:
            assert res.json()["code"] == 0
            assert res.json()["sv"] == 0
        except:
            send_dingding("特权详情", self.module, api_text)
            assert False


    @allure.title("特权分页列表v2")
    @pytest.mark.parametrize("test_input, expect", test_data["test_11"])
    def test_11(self, base_url, common_session, test_input, expect):
        '''特权分页列表v2'''
        url = base_url + "/product-api/vipPrivilege/list/v2/" + test_input["id"]
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert res.json()["sv"] == expect["sv"]
        except:
            try:
                assert res.json()["code"] == expect["code"]
                assert expect["message"] in res.json()["message"]
            except:
                send_dingding("特权分页列表v2", self.module, api_text)
                assert False


    @allure.title("特权-供应商列表")
    @pytest.mark.parametrize("test_input, expect", test_data["test_12"])
    def test_12(self, base_url, common_session, test_input, expect):
        '''特权-供应商列表'''
        url = base_url + "/product-api/vipPrivilege/offer/list"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert res.json()["sv"] == expect["sv"]
        except:
            try:
                assert res.json()["code"] == expect["code"]
                assert expect["message"] in res.json()["message"]
            except:
                send_dingding("特权-供应商列表", self.module, api_text)
                assert False


    @allure.title("特权分页下发")
    def test_13(self, base_url, common_session):
        '''特权分页下发'''
        url = base_url + "/product-api/vipPrivilege/list/1"
        res = common_session.get(url)
        api_text = res.text
        try:
            assert res.json()["code"] == 0
            assert res.json()["sv"] == 0
        except:
            send_dingding("特权分页下发", self.module, api_text)
            assert False

    @allure.title("卡包权益下发")
    @pytest.mark.parametrize("test_input, expect", test_data["test_14"])
    def test_14(self, base_url, common_session, test_input, expect):
        '''卡包权益下发'''
        url = base_url + "/product-api/vipPrivilege/pack"
        res = common_session.get(url, params = test_input)
        api_text = res.text
        try:
            assert res.json()["code"] == expect["code"]
            assert res.json()["message"] == expect["message"]
        except:
            try:
                assert res.json()["code"] == expect["code"]
            except:
                send_dingding("卡包权益下发", self.module, api_text)
                assert False
