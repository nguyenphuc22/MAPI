import time
from datetime import datetime, timedelta
import keylogger_server
import shutdown_logout_server
import win32com.client
import app_process_server
import directory_tree_server
import live_screen_server
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
islock = 0
havePath = 0
machineState = 1

listName = list()
listPid = list()
listProcess = list()

def utilPath(rep):
    return rep.split("\n")[-1]

def sendBack(subject,body,sendTo,path):
    repMailItem = win32com.client.Dispatch("Outlook.Application").CreateItem(0)
    repMailItem.Subject = subject
    repMailItem.BodyFormat = 1
    repMailItem.Body = body
    repMailItem.To = sendTo
    if path:
        repMailItem.Attachments.Add(path)
    repMailItem.Display()
    repMailItem.Send()

def listen(msg):
    global islock,machineState,listName,listPid,listProcess,havePath
    string = msg.lower().strip().split()
    rep = ""
    if "mapi" == string[0]:
        if "keyboard" == string[1]:
            if "lock" == string[2]:
                if islock == 1:
                    rep = "The keyboard state is block"
                else:
                    rep, islock = keylogger_server.keylog(msg,islock)
            elif "unlock" == string[2]:
                if islock == 0:
                    rep = "The keyboard state is unblock"
                else:
                    rep, islock = keylogger_server.keylog(msg, islock)
            elif "state" == string[2]:
                if islock == 1:
                    rep = "The keyboard state is block"
                else:
                    rep = "The keyboard state is unblock"
        if "system" == string[1]:
            if "shutdown" == string[2]:
                machineState = 0
                rep = "The system is shutdown"
            elif "logout" == string[2]:
                machineState = 2
                rep = "The system is logout"
        if "soft" == string[1]:
            if "list" == string[2]:
                listName,listPid,listProcess = app_process_server.app_process(msg)
                rep ="\n".join(listName)
            if "kill" == string[2]:
                rep = app_process_server.app_process(msg)
            if "start" == string[2]:
                rep = app_process_server.app_process(msg)
        if "file" == string[1]:
            if "list" == string[2]:
                rep = directory_tree_server.getTree(msg)
            if "send" == string[2]:
                havePath = 1
                rep = directory_tree_server.getPathFile(msg)
        if "screen" == string[1]:
            if "scap" == string[2]:
                havePath = 1
                rep = live_screen_server.capture_screenNow()

    return msg + "\nREP:\n" + rep

inbox = outlook.GetDefaultFolder(6)
messages = inbox.Items
mailDefault = messages.GetLast()

while True:
    mailNow = messages.GetLast()
    if( mailNow.ReceivedTime > mailDefault.ReceivedTime ):
        if( "hi bot" in mailNow.subject.lower()):
            rep = listen(mailNow.Body)
            print(rep)
            if havePath == 1:
                sendBack("I'm bot",rep,mailNow.Sender.GetExchangeUser().PrimarySmtpAddress,path=utilPath(rep))
            else:
                sendBack("I'm bot", rep, mailNow.Sender.GetExchangeUser().PrimarySmtpAddress,path="")
            mailDefault = mailNow
            print(True)

        if machineState == 0:
            shutdown_logout_server.shutdown_logout("shutdown")
        elif machineState == 2:
            shutdown_logout_server.shutdown_logout("logout")
    else:
        print(False)
    havePath = 0
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