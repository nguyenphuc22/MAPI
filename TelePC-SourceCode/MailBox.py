import win32com.client
import Email

class MailBox:
    def __init__(self):
        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        inbox = outlook.GetDefaultFolder(6)
        self.mails = inbox.Items
        print("Init")

    def getNewMail(self):
        print("NewMail")
        return Email.Email(self.mails.GetLast())

    def getUnreadMails(self):
        result = filter(lambda x : x.UnRead == True,self.mails)
        mails = list()
        for message in result:
            mails.append(Email.Email(message))
        return mails
