from .FileConCtrl import FileConCtrl
from json import dumps as jsonencode
from json import loads as jsondecode


class DataArray:
    def __init__(self, filePath):
        self.dataArray = []
        self.fileCtrl = FileConCtrl(filePath)
        json_datatmp = self.fileCtrl.read(AUTOCREATE=1)
        if json_datatmp != "":
            self.dataArray = jsondecode(json_datatmp)

    def get(self):
        return self.dataArray

    def getbyId(self, id):
        return self.dataArray[id]

    def add(self, new):
        self.dataArray.append(new)
        self.fileCtrl.write_cover(jsonencode(self.dataArray))

    def clear(self):
        self.dataArray = []
        self.fileCtrl.write_cover(jsonencode(self.dataArray))

    def delbyId(self, id):
        self.dataArray.pop(int(id))
        self.fileCtrl.write_cover(jsonencode(self.dataArray))
