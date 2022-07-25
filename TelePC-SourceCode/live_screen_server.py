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

def capture_screen(client):
    INFO_SZ = 100
    while client:
        img = ImageGrab.grab()
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        data = img_bytes.getvalue()
        
        # send frame size
        client.sendall(bytes(str(len(data)), "utf8"))

        # send frame data
        client.sendall(data)

        # listen to next command from client: continue or back
        check_stop = client.recv(INFO_SZ).decode("utf8")
        if("STOP_RECEIVING" in check_stop):
            break


            



