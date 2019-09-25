import copy


class CreateJson():
    def __init__(self):
        pass

    def createJsonData(self,jsondata,jsonkeyslist = []):

        copyjson = copy.copy(jsondata)
        if jsonkeyslist is not None:
            for keys in jsonkeyslist:
                pass
