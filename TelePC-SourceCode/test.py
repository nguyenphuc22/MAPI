import keylogger_server
import app_process_server

ls1,ls2,ls3 = app_process_server.app_process("mapi soft list")
print(ls1)
rep = "The List Software Running" + "\n" + "\n".join(ls1)
print(rep)