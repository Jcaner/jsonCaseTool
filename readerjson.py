#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 10:13
# @Author  : dongpf
# @Site    :
# @File    : readerjson.py
# @Software: PyCharm

from functools import reduce
from operator import getitem


class ReaderJson(object):
    __value = list()
    __key = list()

    def getJsonKey(self, jsondata):
        '''
        获得json的所有key
        :param jsondata:
        :return: list
        '''

        if isinstance(jsondata, list):
            for j in jsondata:
                if isinstance(j, list):
                    print(j, '---j')
                    for i in j:
                        self.getJsonKey(i)
                elif isinstance(j, dict):
                    for k, v in j.items():
                        print(k, '---k')
                        self.getJsonKey(v)
        elif isinstance(jsondata, dict):
            for m, n in jsondata.items():
                print(m, '---m')
                self.getJsonKey(n)

    def getJsonValue(self, jsondata, jsonpaths = []):
        '''
        获得json的所有路径的value
        :param jsondata: json格式的数据
        :param jsonpaths: 从getJsonPath中获得的list，默认为[]时会自动获取
        :return: list
        '''
        if jsonpaths is None:
            jsonpaths = self.getJsonPath(jsondata)
            print(jsonpaths)
        __values = []
        for keylist in jsonpaths:
            value = reduce(lambda a, b: getitem(a, b), keylist, jsondata)
            __values.append(value)

        return __values

    def getJsonPath(self, jsondata):
        '''
        获得json的全部路径
        eg：
           [
                ['guid'], ['name'], ['is_active'], ['company'], ['address'], ['registered'], ['latitude'], ['longitude'],
                ['tags'], ['tags', 0], ['tags', 1], ['tags', 2],
                ['sites'],
                ['sites', 0],
                ['sites', 0, 'name'], ['sites', 0, 'name', 'k'], ['sites', 0, 'url'],
                ['sites', 1], ['sites', 1, 'name'], ['sites', 1, 'url'],
                ['sites', 2], ['sites', 2, 'name'], ['sites', 2, 'url']
            ]

        :param jsondata: json格式的数据
        :return: list
        '''

        paths = []
        if isinstance(jsondata, dict):
            for k, v in jsondata.items():
                paths.append([k])
                paths += [[k] + x for x in self.getJsonPath(v)]

        elif isinstance(jsondata, list):  # and not isinstance(jsondata, str)
            for i, v in enumerate(jsondata):
                paths.append([i])
                paths += [[i] + x for x in self.getJsonPath(v)]
        return paths

