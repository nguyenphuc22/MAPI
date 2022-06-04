import pygame
from pygame import mixer
import threading


class SingletonMeta(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance
        return self._instances[self]


class ManagerAudio(metaclass=SingletonMeta):

    def __init__(self, email, paths):
        self.mymail = email
        pygame.init()
        mixer.init()
        for path in paths:
            print(path)
            mixer.music.load(path)

    def play(self):
        mixer.music.play()
        self.thread = threading.Thread(target=self.update_audio, args=())
        self.thread.daemon = True
        self.thread.start()

    def update_audio(self):
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def pause(self):
        mixer.music.pause()

    def unpause(self):
        mixer.music.unpause()

    def stop(self):
        mixer.music.stop()
        self.thread.join()