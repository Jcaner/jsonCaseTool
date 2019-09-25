class WriterJson():
    '''
    单例设计模式
    WriterJson(newjson)() 进行调用
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
        '''
        返回新文件名
        :return: str
        '''
        self.n = self.n +1
        return 'jsoncase/jsoncase'+str((self.n))+'.txt'

    def __call__(self, *args, **kwargs):
        with open(self.newFilenamePath(),'w+',encoding = 'utf-8') as f:
            f.write(self.newjson)
