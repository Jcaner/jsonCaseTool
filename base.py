#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 10:13
# @Author  : dongpf
# @Site    :
# @File    : base.py
# @Software: PyCharm

import json
import yaml


# TODO:1.增加不需要容错的关键参数过滤功能
# TODO:2.增加发送JSON的功能
# TODO:3.'111'是json问题,isJson()

class Base():
    def __init__(self):
        self.__filename = 'jsondata.txt'
        self.__casesGenerateMolds = 'casesGenerateMolds.json'

    def readYaml(self):
        with open('caseelement.yaml', 'r', encoding = 'utf-8') as yamlcaseelement:
            return yaml.load(yamlcaseelement.read(), Loader = yaml.FullLoader)

    def readYamlcaseElement(self):
        '''
        #读取yaml文件
        :return: list
        '''
        return self.readYaml()['elements']

    def getCaseElementNum(self):
        '''

        :return: 返回yaml中element数量
        '''
        return len(self.readYaml()['elements'])

    def isJson(self, data):
        '''
        判断内容是否是json
        :param data:
        :return: T/F
        '''
        if isinstance(data, str):
            try:
                json.loads(data, encoding = 'utf-8')
            except ValueError as e:
                print(e)
                return False
            return True
        else:
            return False

    def toStr(self,jsondata):
        if isinstance(jsondata,dict):
            jsondata = json.dumps(jsondata,indent=4)
        return jsondata

    def toJson(self, jsonstr):
        '''
        如果是str，则转换成json
        :param jsonstr:
        :return: json
        '''

        if isinstance(jsonstr, str):
            jsondata = json.loads(jsonstr)
        return jsondata

    def jsonDatafile(self):
        '''
        从文件获取jsondata.txt 的内容
        :return:
        '''
        with open(self.__filename, 'r', encoding = 'utf-8') as data:
            self.__jsondata = data.read()
        return self.__jsondata

    @property
    def jsonfilename(self):
        return self.__filename

    @jsonfilename.setter
    def jsonfilename(self, value):
        self.__filename = value


    def readCasesGenerateMoldsJson(self):
        with open(self.__casesGenerateMolds,'r',encoding = 'utf-8') as cases:
            jsoncasesBases = cases.read()
        return jsoncasesBases

    @property
    def casesGenerateMolds(self):
        return self.__casesGenerateMolds

    @jsonfilename.setter
    def casesGenerateMolds(self, value):
        self.__casesGenerateMolds = value
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

if __name__ == '__main__':
    b = Base()
    print(b.readCasesGenerateMoldsJson())