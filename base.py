import json
import yaml




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

class Base():

    '''
    读取yaml文件
    '''
    def __init__(self):
        self.__filename = 'jsondata.txt'

    def readYaml(self):
         with open('caseelement.yaml','r',encoding='utf-8') as yamlcaseelement:
            return yaml.load(yamlcaseelement.read())
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


    def isJson(self,data):
        '''
        判断内容是否是json
        :param data:
        :return: T/F
        '''
        if isinstance(data,str):
            try:
                json.loads(data,encoding='utf-8')
            except ValueError as e:
                print(e)
                return False
            return True
        else:
            return False

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


















