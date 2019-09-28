#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 10:13
# @Author  : dongpf
# @Site    :
# @File    : runnerjson.py
# @Software: PyCharm

import datetime

from tomorrow3 import threads

from base import Base
from writerjson import WriterJson
from createjson import CreateJson
from readerjson import ReaderJson

create = CreateJson()
bs = Base()

class RunnerJson():

    def runnerTest(self, floor: int):
        '''
        1.获取数据源 √
        2.获取json全路径 √
        3.获取yaml参数 √
        4.组装
        5.输出到jsoncase/xxxx.txt
        '''
        nums = bs.getCaseElementNum()
        for i in range(nums):
            if floor >= 1:
                self.runnercore(floor, nums, i, type = 1)
            elif floor == 0:
                self.runnercore(floor, nums, i, type = 2)

    @threads(10)
    def runnercore(self, floor, nums, i, type):

        if type == 1:
            # 固定循环方式组成固定用例 与初始化迭代器指针对应
            [create.cycleCase.__next__() for _ in range(i + 1)]
            newjson = create.createjson(floor, -1)
            WriterJson(bs.toStr(newjson))()
            while True:  # 初始化迭代器指针
                if create.cycleCase.__next__() == bs.readYamlcaseElement()[nums - 1]:
                    break

        if type == 2:
            # 只修改json中一个key的值
            for k in range(len(ReaderJson().getJsonPath(bs.toJson(bs.jsonDatafile())))):
                newjson = create.createjson(floor, k)
                WriterJson(bs.toStr(newjson))()


if __name__ == '__main__':
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '执行中...')
    R = RunnerJson()
    # 批量修改1-4级目录生成case
    [R.runnerTest(i) for i in range(0, 5)]
    # 1-4级目录中只修改一个元素
