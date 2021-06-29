import os

generate_report = "pytest --alluredir ./report/allure_raw"
os.system(generate_report) # 在命令行输入生成报告的命令

load_report = "allure serve report/allure_raw"
os.system(load_report) # 在命令行输入加载报告的命令
