import app_process_server

class SingletonMeta(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args,**kwargs)
            self._instances[self] = instance
        return self._instances[self]


class ManagerSoft(metaclass=SingletonMeta):
    def __init__(self,email):
        self.mymail = email

    def list(self,msg,_callBack = None):
        listName, listPid, listProcess = app_process_server.app_process(msg)
        rep = "\n".join(listName)
        if _callBack:
            _callBack(self.mymail.getSender(), self.mymail.getSubject(), self.mymail.getBody(), rep)
        self.mymail.sendBack(rep,"")

    def kill(self,msg,_callBack = None):
        rep = app_process_server.app_process(msg)
        if _callBack:
            _callBack(self.mymail.getSender(), self.mymail.getSubject(), self.mymail.getBody(), rep)
        self.mymail.sendBack(rep,"")

    def start(self,msg,_callBack = None):
        rep = app_process_server.app_process(msg)
        if _callBack:
            _callBack(self.mymail.getSender(), self.mymail.getSubject(), self.mymail.getBody(), rep)
        self.mymail.sendBack(rep,"")