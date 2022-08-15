import os

import pythoncom
import win32com.client
from EmailInterface import EmailInterface


def utilPath(rep):
    return rep.split("\n")[-1]

class OutLook(EmailInterface):


    def __init__(self,mail):
        self.mail = mail

    def isValidate(self) -> bool:
        return super().isValidate()

    def isKey(self,key_s) -> bool:
        return super().isKey(key_s)

    def getSubject(self) -> str:
        return self.mail.subject

    def getBody(self) -> str:
        self.mail.UnRead = False
        return self.mail.Body

    def getFiles(self) -> list:
        result = list()
        for attachment in self.mail.Attachments:
            print(os.path.join(os.path.abspath("Audio"),str(attachment)))
            attachment.SaveAsFile(os.path.join(os.path.abspath("Audio"),str(attachment)))
            result.append(os.path.join(os.path.join(os.path.abspath("Audio"),str(attachment))))
        return result

    def getUnRead(self) -> bool:
        return self.mail.UnRead

    def getSender(self) -> str:
        pythoncom.CoInitialize()
#        if self.mail.SenderEmailType == "EX":
        return self.mail.Reply().To
#        return self.mail.SenderEmailAddress

    def sendBack(self, body, path):
        pythoncom.CoInitialize()
        repMailItem = self.mail.Reply()
        repMailItem.Subject = "I'm bot"
        repMailItem.BodyFormat = 1
        repMailItem.Body = body
        #repMailItem.To = self.getSender()
        print(path)
        print(utilPath(path))
        if path:
            try:
                repMailItem.Attachments.Add(utilPath(path))
            except:
                repMailItem.Body = "The file you're attaching is bigger than the server allows. Try putting the file in a shared location and sending a link instead."
        #repMailItem.Display()
        repMailItem.Send()
