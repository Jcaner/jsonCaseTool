import datetime
from base import Base
from writerjson import WriterJson
from createjson import CreateJson
from tomorrow3 import threads


class RunnerJson(CreateJson):

    def runnerTest(self,floor:int):
        '''
        1.获取数据源 √
        2.获取json全路径 √
        3.获取yaml参数 √
        4.组装
        5.输出到jsoncase/xxxx.txt
        '''
        nums = Base().getCaseElementNum()
        jsondata = Base().toJson(Base().jsonDatafile())
        for i in range(nums):
            self.runnercore(floor,nums,jsondata,i)

    @threads(10)
    def runnercore(self,floor,nums,jsondata,i):
        # 固定循环方式组成固定用例 与初始化迭代器指针对应
        [self.cycleCase.__next__() for _ in range(i + 1)]
        newjson = self.createjson(jsondata, floor)
        WriterJson(str(newjson))()
        while True:  # 初始化迭代器指针
            if self.cycleCase.__next__() == Base().readYamlcaseElement()[nums - 1]:
                break


if __name__ == '__main__':
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'执行中...')
    R = RunnerJson()
    [R.runnerTest(i) for i in range(1,5)] #生成case