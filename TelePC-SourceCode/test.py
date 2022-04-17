import FactoryOutLook

mails = FactoryOutLook.FactoryOutLook().createMailBox("Nickseven123","Hahahaha")

for mail in mails:
    print(mail.getBody())