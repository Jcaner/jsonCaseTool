import os
import sys
import json
import requests
from tomorrow3 import threads
import yaml
import time

#TODO:1.增加不需要容错的关键参数过滤功能
#TODO:2.增加发送JSON的功能
#TODO:3.'111'是json问题,isJson()

jsonstr = '''
{"code":0,"message":"success","resultData":{"footerImageArray":[{"$$hashKey":"00G","footerImageURL":"http://cdn.oudianyun.com/gxej-bco/dev/osc/1536997739916_73.84672722703918.png","footerImageName":"微信公众号"},{"$$hashKey":"00L","footerImageURL":"http://cdn.oudianyun.com/gxej-bco/dev/osc/1536997797803_89.28036273241464.png","footerImageName":"下载客户端"},{"$$hashKey":"00W","footerImageURL":"http://cdn.oudianyun.com/gxej-bco/stg/osc/1546929242381_57.92603252833359.png","footerImageName":"页尾图片名称圈圈圈"},{"$$hashKey":"00J","footerImageURL":"http://cdn.oudianyun.com/gxej-bco/stg/osc/1548656588972_91.1532866641156.png","footerImageName":"尾页测试"}],"footerPhoneName":"热线电话","footerPhoneArray":["400 628 6121","400 628 6122"],"footerWorktimeName":"周一至周五","footerWorktime":"9：00 ~ 18：00","companyId":171}}
'''

'''
通过文件的JSON串获取到json容错的用例

cmd >> python 文件路径 需要保存的路径


'''

class Base(object):

    '''
    读取yaml文件
    '''
    def __init__(self):
        self.__filename = 'jsondata.txt'

    def readYaml(self):
         with open('caseelement.yaml','r',encoding='utf-8') as yamlcaseelement:
            return yaml.load(yamlcaseelement.read())
    def readYamlcaseElement(self):
        #读取yaml文件返回list
        return self.readYaml()['elements']
    def getCaseElementNum(self):
        #返回yaml中element数量
        return len(self.readYaml()['elements'])


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

    def jsonDatafile(self):
        #获取jsondata.txt 的内容
        with open(self.__filename,'r',encoding='utf-8') as data:
            self.__jsondata = data.read()
        return self.__jsondata

    @property
    def jsonfilename(self):
        return self.__filename

    @jsonfilename.setter
    def jsonfilename(self,value):
        self.__filename = value

'''
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

'''
  

class RunJsonTool():
    def __init__(self):
        self.path = None
        self.fileName = None

    def __call__(self,path,fileName):
        self.fileName  = fileName
        self.path = path
        self.run()
    
    def run(self):
        #获取json文件
        pass


class ReaderJson():
    __value = list()
    __key = list()
    __path = list()
    def toJson(self, jsonstr):
        if isinstance(jsonstr, str):
            jsondata = json.loads(jsonstr)
        return jsondata

    def readJsonKey(self, jsondata):
        '''
        :param jsondata:
        :return:
        '''

        if isinstance(jsondata, list):
            for j in jsondata:
                if isinstance(j, list):
                    print(j,'---j')
                    for i in j:
                        self.readJsonKey(i)
                elif isinstance(j, dict):
                    for k, v in j.items():
                        print(k,'---k')
                        self.readJsonKey(v)
        elif isinstance(jsondata, dict):
            for m, n in jsondata.items():
                print(m,'---m')
                self.readJsonKey(n)


    def readJsonValue(self, jsondata):
        if isinstance(jsondata, list):
            for i in jsondata:
                self.readJsonValue(i)
        elif isinstance(jsondata, dict):
            for _, v in jsondata.items():
                self.readJsonValue(v)
        else:
            # print(jsondata)
            self.__value.append(jsondata)

    def readJsonPath(self,jsondata,jsonpath =[]):
        '''
        :param jsondata:
        :return:
            [
                guid,name,is_active,company,address,registered,latitude,longitude,tags,
                sites,[sites,0,name],[sites,0,url],[sites,1,name],[sites,1,url],[sites,2,name],[sites,2,url]
            ]
        '''

        #['guid', 'name', 'is_active', 'company', 'address', 'registered', 'latitude', 'longitude', 'tags', 'sites', 0, 'name', 'k', 0, 'url', 1, 'name', 1, 'url', 2, 'name', 2, 'url']

        if isinstance(jsondata, list):

            for j,n in zip(jsondata,range(len(jsondata))):

                if isinstance(j, list):
                    self.__path.append(n)
                    for i in j:
                        self.readJsonPath(i)
                elif isinstance(j, dict):
                    for k, v in j.items():

                        self.__path.append(n)
                        self.__path.append(k)
                        #print(k,'---k')
                        #print(self.__path)
                        self.readJsonPath(v)

        elif isinstance(jsondata, dict):
            for m, n in jsondata.items():
                print(m,'---m')
                #path = path.append(m)
                #path = jsonpath.append(m)
                #print(self.__path)
                self.__path.append(m)
                self.readJsonPath(n)

    def jsonpath(self):
        return self.__path



class WriterJson():
    '''
    将json写入到文件中
    '''
    init_flag = False
    instance = None
    def __init__(self,newjson):
        if self.init_flag is False:
            self.n = 0
            self.init_flag = True

        self.newjson =newjson

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance  = super().__new__(cls)
        return cls.instance

    def newFilenamePath(self):
        self.n = self.n +1
        return 'jsoncase/jsoncase'+str((self.n))+'.txt'

    def __call__(self, *args, **kwargs):
        with open(self.newFilenamePath()) as f:
            f.write(self.newjson)


class CreateJson():
    def __init__(self):
        pass


    @threads(10)
    def createJsonData(self,jsondata,jsonpath = None):
       pass





if __name__ == '__main__':


    a = ReaderJson()
    b = Base()
    a.readJsonPath(a.toJson(b.jsonDatafile()))
    print(a.jsonpath())



'''
if __name__ == '__main__':
    a = ReaderJson()
    b = Base()
    a.readJsonKey(a.toJson(b.jsonDatafile()))
    #a.readJsonValue(a.toJson(jsonstr))
    #jsons = a.toJson(jsonstr)
    #print(jsons['resultData']['footerImageArray'][1]['footerImageName'])
    #b  = Base()
    #b.jsonfile= 'aaa.txt'

    #print(b.isJson('111'))


if __name__ == "__main__":
    path = sys.argv[1]
    filename = sys.argv[2]
    print('---------json容错case正在生成----------')
    RunJsonTool(path,filename)
    print('---------生成case成功------------------')
'''


