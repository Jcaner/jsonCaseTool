#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 10:13
# @Author  : dongpf
# @Site    :
# @File    : createjson.py
# @Software: PyCharm

from copy import deepcopy
from itertools import cycle

from base import Base
from readerjson import ReaderJson


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
        self.yamlelements = Base().readYamlcaseElement()
        self.jsonpath = ReaderJson().getJsonPath(Base().toJson(Base().jsonDatafile()))
        self.cycleCase = cycle(self.yamlelements)
        self.jsons = Base().toJson(Base().jsonDatafile())

    def createjson(self, floor, i):
        '''
        修改每层目录的json生成用例
        :return: new json case
        '''
        newjson = deepcopy(self.jsons)
        if i < 0:
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
        if i >= 0:
            # 获取指定的list的元素
            v = self.jsonpath[i]
            if len(v) == 1:
                newjson[v[0]] = self.cycleCase.__next__()
            elif len(v) == 2:
                newjson[v[0]][v[1]] = self.cycleCase.__next__()
            elif len(v) == 3:
                newjson[v[0]][v[1]][v[2]] = self.cycleCase.__next__()
            elif len(v) == 4:
                newjson[v[0]][v[1]][v[2]][v[3]] = self.cycleCase.__next__()
            else:
                raise Exception('请修改代码')
            '''
            问题，修改了前面的，后面找不到对应的json了
            '''
            print('---------', newjson, len(v), len(self.jsonpath), i)
            return newjson
