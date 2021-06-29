import pytest
import requests

def get_access_token():
    '''获取access_token'''
    url = "http://hk-test.showcard.vip/user-api/user/thirdLogin/facebook"
    body = {
        "thirdUserId": "156825156459002",
        "thirdToken": "EAAKqynAtHIYBAEc0dZA2Me90Q68ZAKf2XjUXGHU0nhMqflLIu7CNY4C362yriOvW5h408w9QaNvuHDt8XAcsQjHPDchKL0YSfnIO3DNCLpRApD0tYdIwQznw4b6IEPDpX4N8uF5ICB5GRVGQQBTO1TrlIlq8G97K2lpkTJ48YToaFdBkEyzQXSz5vn1Wf4JYsMpfiX9FAA4cyHZAw1hkxfLSs9axYIfEBZCbZAllKUQZDZD"
    }
    res = requests.post(url, data=body)
    access_token = res.json()["body"]["userInfo"]["accessToken"]
    # print(res.text)
    # print(access_token)
    return access_token


@pytest.fixture(name="common_session")
def common_session():
    '''公共session，头部传入access token'''
    access_token = get_access_token()
    s = requests.Session()
    head = {
        "Authorization": "Bearer " + access_token
    }
    s.headers.update(head)
    # print(s.headers)
    yield  s
    s.close()


@pytest.fixture(scope="session")
def url(base_url):
    return base_url


# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     # 获取钩子方法的运行结果
#     out = yield
#
#     # 从钩子方法的调用结果中获取测试报告
#     report = out.get_result()
#     if report.when == "call":
#         print("测试报告: %s" % report)
#         print("步骤: %s" % report.when)
#         print("nodeid: %s" % report.nodeid)
#         print("description: %s" % str(item.function.__doc__))
#         print("运行结果： %s" % report.outcome)
#
#         if report.outcome == "failed":

