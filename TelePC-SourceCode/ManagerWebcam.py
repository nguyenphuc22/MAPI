import os
import threading
import time

import cv2
import directory_tree_server


class SingletonMeta(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args,**kwargs)
            self._instances[self] = instance
        return self._instances[self]


class ManagerWebcam(metaclass=SingletonMeta):

    def __init__(self,email):
        self.mymail = email
    #    self.cam = cv2.VideoCapture(0)


    def turnOn(self,_callBack = None):
        self.cam = cv2.VideoCapture(0)
        if(self.cam.isOpened()):
            self.mymail.sendBack("Webcam turn on", "")
            if _callBack:
                _callBack(self.mymail.getSender(), self.mymail.getSubject(), self.mymail.getBody(), "Webcam turn on")
            self.isRun = True
            self.thread = threading.Thread(target=self.show, args=())
            self.thread.daemon = True
            self.thread.start()


    def turnOff(self,_callBack = None):
        if(self.cam.isOpened()):
            self.mymail.sendBack("Webcam turn off", "")
            if _callBack:
                _callBack(self.mymail.getSender(), self.mymail.getSubject(), self.mymail.getBody(), "Webcam turn off")
            print("turn off")
            self.cam.release()
            self.isRun = False
            self.thread.join()
            cv2.destroyAllWindows()
            cv2.waitKey(1)


    def show(self):
        while self.isRun:
            if self.cam.isOpened():
                (self.status, self.frame) = self.cam.read()
            time.sleep(.01)

    def showFrame(self):
        # Display frames in main program
        cv2.imshow('frame', self.frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            self.turnOff()
        if key == ord('c'):
            self.capPicture()

    def capPicture(self,_callBack = None):
        if (self.cam.isOpened()):
            time.sleep(1)
            (self.status, self.frame) = self.cam.read()
            time.sleep(1)
            timeNow = time.time() * 1000
            img_name = r"Attachments\{}.png".format(timeNow)
            cv2.imwrite(img_name, self.frame)
            time.sleep(1)
            print("{} written!".format(img_name))
            rep = os.path.abspath(img_name)
            print(rep)
            print(os.path.abspath("Attachments"))
            print(img_name)
            print(os.path.abspath(img_name))

            self.mymail.sendBack(img_name, rep)
            if _callBack:
                _callBack(self.mymail.getSender(), self.mymail.getSubject(), self.mymail.getBody(), img_name)
        else:
            print("Acess Webcam Error")
            if _callBack:
                _callBack(self.mymail.getSender(), self.mymail.getSubject(), self.mymail.getBody(), "Access Webcam Error")
            self.mymail.sendBack("Access Webcam Error", "")