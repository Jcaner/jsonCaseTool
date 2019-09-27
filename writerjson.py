#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 10:13
# @Author  : dongpf
# @Site    :
# @File    : writerjson.py
# @Software: PyCharm


class WriterJson():
    init_flag = False
    instance = None

    def __init__(self, newjson):
        if self.init_flag is False:
            self.n = 0
            self.init_flag = True

        self.newjson = newjson

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def newFilenamePath(self):
        # 返回新文件名
        self.n = self.n + 1
        return 'jsoncase/jsoncase' + str((self.n)) + '.txt'

    def __call__(self, *args, **kwargs):
        with open(self.newFilenamePath(), 'w+', encoding = 'utf-8') as f:
            f.write(self.newjson)


if __name__ == '__main__':
    WriterJson('11111')()
