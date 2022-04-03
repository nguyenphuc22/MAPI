import os

class SingletonMeta(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args,**kwargs)
            self._instances[self] = instance
        return self._instances[self]


class ManagerSystem(metaclass=SingletonMeta):
    def __init__(self,email):
        self.mymail = email

    def shutdown(self):
        self.mymail.sendBack("The system is shutdown")
        os.system('shutdown -s -t 15')

    def logout(self):
        self.mymail.sendBack("The system is logout")
        os.system('shutdown -l')