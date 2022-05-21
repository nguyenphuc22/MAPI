import win32com.client
from EmailInterface import EmailInterface


def utilPath(rep):
    return rep.split("\n")[-1]

class OutLook(EmailInterface):

    
    def __init__(self,mail):
        self.mail = mail

    def isValidate(self) -> bool:
        return super().isValidate()

    def getSubject(self) -> str:
        return self.mail.subject

    def getBody(self) -> str:
        self.mail.UnRead = False
        return self.mail.Body

    def getFiles(self) -> list:
        return self.mail.Attachments

    def getUnRead(self) -> bool:
        return self.mail.UnRead

    def getSender(self) -> str:
        return self.mail.Sender.GetExchangeUser().PrimarySmtpAddress

    def sendBack(self, body, path):
        repMailItem = win32com.client.Dispatch("Outlook.Application").CreateItem(0)
        repMailItem.Subject = "I'm bot"
        repMailItem.BodyFormat = 1
        repMailItem.Body = body
        repMailItem.To = self.getSender()
        if path:
            repMailItem.Attachments.Add(utilPath(path))
        repMailItem.Display()
        repMailItem.Send()
