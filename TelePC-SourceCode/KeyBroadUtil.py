from ctypes import *

def block():
    print("Block")
    windll.user32.BlockInput(True)

def unBlock():
    windll.user32.BlockInput(False)
