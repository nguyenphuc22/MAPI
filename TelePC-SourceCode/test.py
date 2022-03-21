import keylogger_server
import app_process_server
import os
import subprocess
import glob
link = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\'
for root,dirs,files in os.walk(link):
    for file in files:
        if file.endswith('.lnk'):
            print(file)
            print(root)

#file_list = glob.glob("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\*.lnk")
#file_list = os.listdir("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs")

acc = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
#print('\n'.join(file_list))
link1 = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\WinRAR\\WinRAR.lnk"

os.startfile(r"{}".format(link1))


