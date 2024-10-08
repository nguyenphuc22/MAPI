import pythoncom
import win32com.client

from Factory import Factory
from OutLook import OutLook

class FactoryOutLook(Factory):
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def createMailBox(self) -> list:
        pythoncom.CoInitialize()
        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        inbox = outlook.GetDefaultFolder(6)
        self.mails = inbox.Items

        result = filter(lambda x: x.UnRead == True, self.mails)
        mails = list()

        for message in result:
            mails.append(OutLook(message))
        return mails