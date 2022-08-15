# Socket
import socket
import pyautogui
import time
# Work with Image
from PIL import ImageGrab
import io

# Thread
from threading import Thread

def capture_screenNow():
    myScreenShot = pyautogui.screenshot()
    timeNow = time.time() * 1000
    myScreenShot.save(r"Attachments\\{}.png".format(timeNow))
    return "{}.png".format(timeNow)
