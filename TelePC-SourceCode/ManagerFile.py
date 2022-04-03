import directory_tree_server

class SingletonMeta(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args,**kwargs)
            self._instances[self] = instance
        return self._instances[self]


class ManagerFile(metaclass=SingletonMeta):
    def __init__(self,email):
        self.state = False
        self.mymail = email

    def list(self,msg):
        rep = directory_tree_server.getTree(msg)
        self.mymail.sendBack(rep,"")

    def send(self,msg):
        rep = directory_tree_server.getPathFile(msg)
        self.mymail.sendBack(rep,rep)