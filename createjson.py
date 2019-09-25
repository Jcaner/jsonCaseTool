from readerjson import ReaderJson
from base import Base
from itertools import cycle



class CreateJson():
    # TODO:
    # 1.如何确定循环数量？range(nums) --->case element的个数
    # 2.如何避免重复eg：元素数与要修改的数量相等或者倍数关系？
    # 3.多线程的化next调用就会被打乱，进行随机操作？
    def __init__(self):
        '''
        基本数据来源支持
        '''
        self.yamlelements =Base().readYamlcaseElement()
        self.jsonpath = ReaderJson().getJsonPath(Base().toJson(Base().jsonDatafile()))

        '''
        无限循环case element，可以__next__()直接调用
        eg:
            elements = self.cycleCase.__next__()
            elements.__next__()
            elements.__next__()
        '''
        self.cycleCase = cycle(self.yamlelements)


    def createOnefloor(self,jsondata):
        '''
        修改一层目录的json生成用例
        :return: new json case
        '''
        newjson = jsondata
        for v in self.jsonpath:
            if len(v) == 1:
                newjson[v[0]] = self.cycleCase.__next__()
        return newjson

    def createTwofloor(self,jsondata):
        '''
        修改二层目录的json生成用例
        :return: new json case
        '''
        newjson = jsondata
        for v in self.jsonpath:
            if len(v) == 2:
                newjson[v[0]][v[1]] = self.cycleCase.__next__()
        return newjson

    def createThreefloor(self,jsondata):
        '''
        修改三层目录的json生成用例
        :return: new json case
        '''
        newjson = jsondata
        for v in self.jsonpath:
            if len(v) == 3:
                newjson[v[0]][v[1]][v[2]] = self.cycleCase.__next__()
        return newjson

    def createFourfloor(self,jsondata):
        '''
        修改四层目录的json生成用例
        :return: new json case
        '''
        newjson = jsondata
        for v in self.jsonpath:
            if len(v) == 4:
                newjson[v[0]][v[1]][v[2]][v[3]] = self.cycleCase.__next__()
        return newjson

    def createjson(self):
        '''
        1.获取数据源 √
        2.获取json全路径 √
        3.获取yaml参数 √
        4.判断每级别目录的个数和case元素的个数，如果能被整除就
        4.组装
        :return: 返回组装好的字典

        '''
        return None


if __name__ == '__main__':

    c = CreateJson()
    for i in range(10):
        jsondata = Base().toJson(Base().jsonDatafile())
        print(c.createOnefloor(jsondata))

    for i in range(10):
        jsondata = Base().toJson(Base().jsonDatafile())
        print(c.createTwofloor(jsondata))

    for i in range(10):
        jsondata = Base().toJson(Base().jsonDatafile())
        print(c.createThreefloor(jsondata))

    for i in range(10):
        jsondata = Base().toJson(Base().jsonDatafile())
        print(c.createFourfloor(jsondata))