### 项目描述

这个一个GCP接口自动化项目，基于python + pytest + requests + allure框架

### 环境准备

1.python
2.pytest
3.requests
4.allure

依赖包安装
>pip install -r requirement.txt

### 运行用例

>1.在文件根目录执行命令：pytest
>2.运行run_all_cases.py文件

### 生成报告

>在文件根目录下运行以下命令：
>pytest --alluredir ./report/allure_raw
>allure serve report/allure_raw


### 目录结构描述

│── cases                            // 测试用例文件夹
│   ├── activity-api                 
│       ├── activity_api.yaml        // activity_api接口数据文件
│		├── test_activity_api.py     // activity_api接口测试用例
│   ├── config-api  
│       ├── config_api.yaml          // config_api接口数据文件
│		├── test_config_api.py       // config_api接口测试用例
│   ├── msg-center-api 
│       ├── msg_center.yaml          // msg_center接口数据文件
│		├── test_msg_center.py       // msg_center接口测试用例
│   ├── Offer-api    
│       ├── offer_api.yaml           // offer_api接口数据文件
│		├── test_offer_api.py        // offer_api接口测试用例
│   ├── pay-api
│       ├── pay_api_api.yaml         // pay_api接口数据文件
│		├── test_pay_api.py          // pay_api接口测试用例 
│   ├── Product-api
│       ├── product_api.yaml         // product_api接口数据文件
│		├── test_product_api.py      // product_api接口测试用例    
│   ├── upgrade-api
│       ├── upgrade_api.yaml         // upgrade_api接口数据文件
│		├── test_upgrade_api.py      // upgrade_api接口测试用例          
│   ├── user-api
│       ├── user_api.yaml            // user_api接口数据文件
│		├── test_user_api.py         // user_api接口测试用例      
│   ├── conftest.py                  // 配置文件
│── common                           // 公共文件
│   ├── db_connect.py                // 数据库配置
│   ├── dingding.py                  // 发送钉钉群机器人
│   ├── hk-king-test.pem             // 数据库密钥      
│   ├── read_yaml.py                 // 读取yaml文件数据
│── report                           // 测试报告
│   ├── allure_raw                   // allure报告源文件
│── get_report.py                    // 生成allure报告文件
│── pytest.ini                       // 公共配置文件
│── readme.MD                        // 帮助文档
│── requirement.txt                  // 相关依赖包
│── run_all_cases.py                 // 运行测试用例
