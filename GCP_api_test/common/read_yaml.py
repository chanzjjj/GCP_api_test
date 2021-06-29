import yaml
import os

def get_yaml(yamlPath):
    if not os.path.isfile(yamlPath):
        raise FileNotFoundError("文件路径不存在，请检查路径是否正确： %s" % yamlPath)
    with open(yamlPath, "r", encoding="utf-8") as fp:
        f = fp.read() # 读出来是字符串
        print(type(f))
    res = yaml.load(f, Loader=yaml.FullLoader)
    print("读取到yaml文件数据")
    print(res)
    return res

if __name__ == '__main__':
    yaml_file = "D:/python_files/GCP_api_test/cases/user-api/user_api.yaml"
    data = get_yaml(yaml_file)
    print(data["test_03"])