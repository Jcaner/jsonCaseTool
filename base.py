import os
import sys
import json
import requests
import tomorrow

#TODO:1.增加不需要容错的关键参数过滤功能
#TODO:2.增加发送JSON的功能

'''
通过文件的JSON串获取到json容错的用例

cmd >> python 文件路径 需要保存的路径


'''

class base(object):
    def __init__(self, data):
        self.data = data
    def readYaml(self):
         with open('caseelement.yaml','r') as yamlcaseelement:
            yaml = yamlcaseelement.read()
         return yaml

    def readYamlcaseElement(self):
        #读取yaml文件返回list
        return readYaml()['elements']

    def getCaseElementNum(self):
        #返回yaml中element数量
        return readYaml().len()

    def isJson(self,data):
        #判断内容是否是json
        if isinstance(data,str):
            try:
                json.loads(data,encoding='utf-8')
            except ValueError as e:
                print(e)
                return False
            return True
        else:
            return False

    @property
    def jsonData(self):
        #获取jsondata.txt 的内容
        with open('jsondata.txt','r') as data:
            self.__jsondata = data.read()
        return self.__jsondata

    @jsonData.setter
    def JsonData(self,josndata):
        # 设置jsondata.txt 的内容
        self.__jsondata = josndata

    @staticmethod
    def getUrlData(url,type,headers,data):
        try:
            if type.upper() == 'GET':
            #发送get请求接受数据
                return requests.get(url=url,headers = headers)
            elif type.upper() == 'POST':
            # 发送post请求接受数据
                return requests.post(url = url, headers = headers,data = data)
        except Exception as e:
            print(e)

  

class RunJsonTool():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = None
        self.fileName = None

    def __call__(self,path,fileName):
        self.fileName  = fileName
        self.path = path
        self.run()
    
    def run(self):
        self.getJson()

    def getJson(self):
        pass
    
    def runJson(self):
        pass

    

if __name__ == "__main__":
    path = sys.argv[1]
    filename = sys.argv[2]
    print('---------json容错case正在生成----------')
    RunJsonTool(path,filename)
    print('---------生成case成功------------------')

