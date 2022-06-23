import threading
from tkinter import *
import MailBox
import FactoryGmailApi
import FactoryOutLook
from tkinter import font
#global var
from tkinter.ttk import Treeview


class MyWinDown:
    def __init__(self,win):
        self.mWin = win

    def initViewLogin(self):
        self.mWin.title('Control Via Email')
        self.mWin.geometry("500x400+10+20")

        self.lbl_title = Label(self.mWin, text="App control via email", fg='black', font=("Helvetica", 18))
        self.lbl_title.place(x = 110, y=30)

        self.lbl_sub = Label(self.mWin, text="", fg='red', font=("Helvetica", 10))
        self.lbl_sub.place(x=140, y=70)

        self.lbl_account = Label(self.mWin, text="Account", fg='black', font=("Helvetica", 12))
        self.lbl_account.place(x=110, y=100)

        self.txtfld_account = Entry(self.mWin, text="Account", bd=2, borderwidth=2, relief="flat" , highlightthickness=2, highlightcolor="#6ED189")
        self.txtfld_account.place(x=110, y=130, width= 300, height= 40)

        self.lbl_password = Label(self.mWin, text="Password", fg='black', font=("Helvetica", 12))
        self.lbl_password.place(x=110, y=175)

        self.txtfld_password = Entry(self.mWin, text="Password", bd=2, borderwidth=2, relief="flat", show='*', highlightthickness=2, highlightcolor="#6ED189")
        self.txtfld_password.place(x=110, y=205, width= 300, height= 40)

        f = font.Font(weight="bold")
        self.btn_Gmail = Button(self.mWin, text="Login with Gmail Api", fg='white',borderwidth=2, relief="flat", bg='#BF4D3B' ,command= lambda : self.checkEmpty("Gmail"))
        self.btn_Gmail.place(x=110, y=265, width= 300, height= 45)
        self.btn_Gmail['font'] = f

        self.btn_Outllook = Button(self.mWin, text="Sign in with Outlook", fg='white', bg='#4665BE', borderwidth=2, relief="flat" ,command= lambda : self.checkEmpty("Outlook"))
        self.btn_Outllook.place(x=110, y=320, width= 300, height= 45)
        self.btn_Outllook['font'] = f

    def destroyViewLogin(self):
        self.lbl_title.destroy()
        self.lbl_sub.destroy()
        self.lbl_password.destroy()
        self.lbl_account.destroy()
        self.btn_Outllook.destroy()
        self.btn_Gmail.destroy()
        self.txtfld_password.destroy()
        self.txtfld_account.destroy()

    def initViewToDo(self):
        self.mWin.title('Hello Python')
        self.mWin.geometry("1000x600+10+20")

        self.lbl_mode = Label(self.mWin, text="Mode:" + self.mode, fg='black', font=("Helvetica", 14))
        self.lbl_mode.place(x=60, y=30)

        self.lbl_account = Label(self.mWin, text= "Account:" + self.account, fg='black', font=("Helvetica", 14))
        self.lbl_account.place(x=60, y=70)

        self.lbl_password = Label(self.mWin, text= "Password:" + self.getPassword(), fg='black', font=("Helvetica", 14))
        self.lbl_password.place(x=60, y=100)

        self.btn_Logout = Button(self.mWin, text="Logout", fg='#6ED189',bg='white', borderwidth=2, relief="flat", highlightthickness=2, highlightbackground="#6ED189",
                                 command=self.logout)
        self.btn_Logout.place(x=745, y=30,height= 100, width= 100)

        self.btn_Run = Button(self.mWin, text="Start", fg='white', bg='#6ED189', borderwidth=2, relief="flat" , command=self.service)
        self.btn_Run.place(x=865, y=30,height= 100, width= 100)


        self.tab = Treeview(self.mWin, height=18, selectmode='browse')
        self.scroll = Scrollbar(self.mWin, orient="vertical", command=self.tab.yview)
        self.scroll.place(x=60,
                          y=190,
                          height=360)

        self.tab.configure(yscrollcommand=self.scroll.set)
        self.tab['columns'] = ("Name", "Subject", "Body", "Rep")
        self.tab.column('#0', width=0)
        self.tab.column("Name", anchor="center", width=150, minwidth=10, stretch=True)
        self.tab.column("Subject", anchor="center", width=150, minwidth=10, stretch=True)
        self.tab.column("Body", anchor="center", width=150, minwidth=10, stretch=True)
        self.tab.column("Rep", anchor="center", width=150, minwidth=10, stretch=True)
        self.tab.heading('#0', text='')
        self.tab.heading("Name", text="Name From")
        self.tab.heading("Subject", text="Subject Email")
        self.tab.heading("Body", text="Body Email")
        self.tab.heading("Rep", text="Rep Email")
        self.tab.place(x=53.0,
                       y=180.0,
                       width=913.0,
                       height=390.0)

    def detroyViewToDo(self):
        self.tab.destroy()
        self.scroll.destroy()
        self.btn_Run.destroy()
        self.lbl_account.destroy()
        self.lbl_password.destroy()
        self.lbl_mode.destroy()

    def service(self):
        if self.btn_Run.cget('text') == "Start":
            self.btn_Run.configure(text= "Stop",fg='white', bg='#CD3B33', borderwidth=2, relief="flat")

            if self.mode == "Outlook":
                self.mailbox = MailBox.MailBox(FactoryOutLook.FactoryOutLook(self.account, self.password))
            else:
                self.mailbox = MailBox.MailBox(FactoryGmailApi.FactoryGmailApi(self.account, self.password))
            self.thread = threading.Thread(target=self.mailbox.start,args=(self.insertTab,))
            self.thread.start()
            self.btn_Logout.configure(fg='#E4E4E4',command='')
        else:
            self.btn_Run.configure(text= "Start",fg='white', bg='#6ED189', borderwidth=2, relief="flat")
            self.mailbox.stop()
            self.thread.join()
            self.btn_Logout.configure(fg='#6ED189',command=self.logout)


    def checkEmpty(self,mode):
        self.mode = mode
        if not self.txtfld_account.get() or not self.txtfld_password.get():
            self.lbl_sub.configure(text = "Account or Password is empty")
        else:
            self.lbl_sub.configure(text = " ")
            self.account = self.txtfld_account.get()
            self.password = self.txtfld_password.get()
            self.destroyViewLogin()
            self.initViewToDo()

    def insertTab(self,sender,subject,body,rep):
        self.tab.insert("", 'end', text="L7",
                        values=(sender,subject,body,rep))

    def getPassword(self):
        result = ""
        for c in self.password:
            result = result + "*"
        return str(result)

    def logout(self):
        self.detroyViewToDo()
        self.initViewLogin()

window = Tk()
MyWinDown(window).initViewLogin()
window.mainloop()