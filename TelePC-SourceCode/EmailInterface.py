import string


class EmailInterface:
    def isValidate(self) -> bool:
        if "hi bot" not in self.getSubject().lower():
            return False
        if "mapi" not in self.getBody().lower():
            return False
        return True
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