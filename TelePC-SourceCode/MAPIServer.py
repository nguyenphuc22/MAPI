import time
from datetime import datetime, timedelta

import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

def sendBack(subject,body,sendTo):
    repMailItem = win32com.client.Dispatch("Outlook.Application").CreateItem(0)
    repMailItem.Subject = subject
    repMailItem.BodyFormat = 1
    repMailItem.Body = body
    repMailItem.To = sendTo

    repMailItem.Display()
    repMailItem.Send()

inbox = outlook.GetDefaultFolder(6)
messages = inbox.Items
mailDefault = messages.GetLast()

while True:
    mailNow = messages.GetLast()
    if( mailNow.ReceivedTime > mailDefault.ReceivedTime ):
        sendBack("I'm bot","Can i hepl you",mailNow.Sender.GetExchangeUser().PrimarySmtpAddress)
        mailDefault = mailNow
        print(True)
    else:
        print(False)

    #print(mailDefault.Sendername)
    #print(mailDefault.subject)
    #print(mailDefault.Body)
    #print(datetime.now().time())
    #print(mailDefault.ReceivedTime.time())
    #print()
    #print(type(mailDefault.ReceivedTime))
    #print(type(datetime.now().time()))
    #print("____________________")
    time.sleep(5)