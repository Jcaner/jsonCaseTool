from readerjson import ReaderJson
from base import Base
from itertools import cycle


class CreateJson():
    '''
    无限循环case element，可以__next__()直接调用
    eg:
        elements = self.cycleCase.__next__()
        elements.__next__()
        elements.__next__()
    '''

    def __init__(self):
        '''
        基本数据来源支持
        '''
        self.yamlelements =Base().readYamlcaseElement()
        self.jsonpath = ReaderJson().getJsonPath(Base().toJson(Base().jsonDatafile()))
        self.cycleCase = cycle(self.yamlelements)

    def createjson(self,jsondata,floor):
        '''
        修改一层目录的json生成用例
        :return: new json case
        '''
        newjson = jsondata
        for v in self.jsonpath:
            if floor == 1:
                if len(v) == 1:
                    newjson[v[0]] = self.cycleCase.__next__()
            elif floor == 2:
                if len(v) == 2:
                    newjson[v[0]][v[1]] = self.cycleCase.__next__()
            elif floor == 3:
                if len(v) == 3:
                    newjson[v[0]][v[1]][v[2]] = self.cycleCase.__next__()
            elif floor == 4:
                if len(v) == 4:
                    newjson[v[0]][v[1]][v[2]][v[3]] = self.cycleCase.__next__()
        return newjson
