import  pickle, psutil, struct
import os

BUFSIZ = 1024 * 4

def send_data(client, data):
    size = struct.pack('!I', len(data))
    data = size + data
    client.sendall(data)
    return

def list_apps():
    ls1 = list()
    ls2 = list()
    ls3 = list()

    cmd = 'powershell "gps | where {$_.mainWindowTitle} | select Description, ID, @{Name=\'ThreadCount\';Expression ={$_.Threads.Count}}'
    proc = os.popen(cmd).read().split('\n')
    tmp = list()
    for line in proc:
        if not line.isspace():
            tmp.append(line)
    tmp = tmp[3:]
    for line in tmp:
        try:
            arr = line.split(" ")
            if len(arr) < 3:
                continue
            if arr[0] == '' or arr[0] == ' ':
                continue

            name = arr[0]
            threads = arr[-1]
            ID = 0
            # interation
            cur = len(arr) - 2
            for i in range (cur, -1, -1):
                if len(arr[i]) != 0:
                    ID = arr[i]
                    cur = i
                    break
            for i in range (1, cur, 1):
                if len(arr[i]) != 0:
                    name += ' ' + arr[i]
            ls1.append(name)
            ls2.append(ID)
            ls3.append(threads)
        except:
            pass
    return ls1, ls2, ls3



def list_processes():
    ls1 = list()
    ls2 = list()
    ls3 = list()
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            name = proc.name()
            pid = proc.pid
            threads = proc.num_threads()
            ls1.append(str(name))
            ls2.append(str(pid))
            ls3.append(str(threads))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return ls1, ls2, ls3

def list_all_appp():
    link = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\'
    lsName = list()
    lsPath = list()
    for root, dirs, files in os.walk(link):
        for file in files:
            if file.endswith('.lnk'):
                lsName.append(file)
                lsPath.append(root + "\\" + file)
    return lsName,lsPath

def kill(pid):
    cmd = 'taskkill.exe /F /PID ' + str(pid)
    try:
        a = os.system(cmd)
        if a == 0:
            return 1
        else:
            return 0
    except:
        return 0
    
def start(name):
    os.system(name)
    return

def app_process(client):
    global msg
    while True:
        msg = client.recv(BUFSIZ).decode("utf8")
        if "QUIT" in msg and len(msg) < 20:
            return
        res = 0
        ls1 = list()
        ls2 = list()
        ls3 = list()
        action = int(msg)
        #0-kill
        if action == 0:
            pid = client.recv(BUFSIZ).decode("utf8")
            pid = int(pid)
            try:
                res = kill(pid)
            except:
                res = 0
        #1-xem
        elif action == 1:
            try:
                status = client.recv(BUFSIZ).decode("utf8")
                if "PROCESS" in status:
                    ls1, ls2, ls3 = list_apps()
                else:
                    ls1, ls2, ls3 = list_processes()
                res = 1
            except:
                res = 0
        #2-xoa
        elif action == 2:
            res = 1
        #3 - start
        elif action == 3:
            pname = client.recv(BUFSIZ).decode("utf8")
            try:
                start(pname)
                res = 1
            except:
                res = 0
        if action != 1 and action != 3:
            client.sendall(bytes(str(res), "utf8"))
        if action == 1:
            ls1 = pickle.dumps(ls1)
            ls2 = pickle.dumps(ls2)
            ls3 = pickle.dumps(ls3)

            send_data(client, ls1)   
            send_data(client, ls2)
            send_data(client, ls3)
    return

def run(msg):
    os.startfile(r"{}".format(msg))

def app_process(msg):

    if "quit" in msg:
        return
    res = 0
    ls1 = list()
    ls2 = list()
    ls3 = list()
    #0-kill
    if "kill" in msg:
        if not ls1:
          ls1,ls2,ls3 = list_apps()
        nameSoft = msg[msg.index("kill") + 4:len(msg)].strip()
        pid = ls2[ls1.index(nameSoft)]
        pid = int(pid)
        try:
            res = kill(pid)
        except:
            res = 0
        return "The Software" + nameSoft + " was killed"
    #1-xem
    elif "list" in msg:
        try:
            if "on" in msg:
                ls1, ls2, ls3 = list_apps()
            elif "all" in msg:
                ls1, ls2 = list_all_appp()
            else:
                ls1, ls2, ls3 = list_processes()
            res = 1
        except:
            res = 0
    #2-xoa
    elif "delete" in msg:
        res = 1
    #3 - start
    elif "start" in msg:
        if not ls2:
            ls1,ls2 = list_all_appp()
        pname = msg[msg.index("start") + 5:len(msg)].strip()
        path = ls2[ls1.index(pname)]
        try:
            run(path)
            res = 1
        except:
            res = 0
        return "The Software" + pname + " was started"


    return ls1, ls2, ls3