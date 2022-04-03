import win32com.client


def utilPath(rep):
    return rep.split("\n")[-1]

class Email:
    def __init__(self,mail):
        self.mail = mail

    def getBody(self):
        self.mail.UnRead = False
        return self.mail.Body

    def getUnRead(self):
        return self.mail.UnRead

    def getSubject(self):
        return self.mail.subject

    def getSender(self):
        return self.mail.Sender.GetExchangeUser().PrimarySmtpAddress

    def isValidate(self):
        if "hi bot" not in self.getSubject().lower():
            return False
        if "mapi" not in self.getBody().lower():
            return False
        return True

    def sendBack(self,body,path):
        repMailItem = win32com.client.Dispatch("Outlook.Application").CreateItem(0)
        repMailItem.Subject = "I'm bot"
        repMailItem.BodyFormat = 1
        repMailItem.Body = body
        repMailItem.To = self.getSender()
        if path:
            repMailItem.Attachments.Add(utilPath(path))
        repMailItem.Display()
        repMailItem.Send()


