import keylogger_server
import app_process_server
import os
import subprocess
import glob
import directory_tree_server
import win32com
import win32com.client
import pyautogui
import time
from datetime import datetime


myScreenShot = pyautogui.screenshot()
timeNow = time.time() * 1000
print(timeNow)
myScreenShot.save(r"C:\\Users\\administrator.HCMUS\\Desktop\\save\\{}.png".format(timeNow))
