import yaml

def readyml(filePath):
    f = open(filePath,'r',encoding='utf-8')
    y = f.read()
    data = yaml.load(y,yaml.FullLoader)
    print(data)
    return data

if __name__ == '__main__':
    s = readyml(r'E:\web_pytest_2020\cases\testdata.yml')
    print(s['test_add_param_article'])