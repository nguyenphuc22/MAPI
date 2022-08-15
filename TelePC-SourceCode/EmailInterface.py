import string


class EmailInterface:
    def isValidate(self) -> bool:
        if "hi bot" not in self.getSubject().lower():
            return False
        if "mapi" not in self.getBody().lower():
            return False
        return True
        pass

    def isKey(self,key) -> bool:
        if len(self.getSubject()) != len(key):
            return False
        if self.getSubject().split(" ")[-1] == key:
            return True
        return False
        pass

    def getBody(self) -> str:
        pass

    def getUnRead(self) -> bool:
        pass

    def getSender(self) -> str:
        pass

    def sendBack(self,body,path):
        pass

    def getSubject(self) -> str:
        pass

    def getFiles(self) -> list:
        pass