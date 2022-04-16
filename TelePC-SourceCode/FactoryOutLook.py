from Factory import Factory

class FactoryOutLook(Factory):

    def createMailBox(self,username,password) -> list:
        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        inbox = outlook.GetDefaultFolder(6)
        self.mails = inbox.Items

        result = filter(lambda x: x.UnRead == True, self.mails)
        mails = list()

        for message in result:
            mails.append(Email.Email(message))

        return mails