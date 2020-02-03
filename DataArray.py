from FileCtrl import FileCtrl
import json


class DataArray:
    def __init__(self, filePath):
        self.dataArray = []
        self.fileCtrl = FileCtrl(filePath)
        jsonDatatmp = self.fileCtrl.read(AUTOCREATE=1)
        if jsonDatatmp != "":
            self.dataArray = json.loads(jsonDatatmp)

    def get(self):
        return self.dataArray

    def getbyId(self, id):
        return self.dataArray[id]

    def add(self, new):
        self.dataArray.append(new)
        self.fileCtrl.write_cover(json.dumps(self.dataArray))

    def clear(self):
        self.dataArray = []
        self.fileCtrl.write_cover(json.dumps(self.dataArray))

    def delbyId(self, id):
        self.dataArray.pop(int(id))
        self.fileCtrl.write_cover(json.dumps(self.dataArray))
