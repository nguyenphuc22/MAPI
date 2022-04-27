import FactoryOutLook
import FactoryGmailApi


mails = FactoryGmailApi.FactoryGmailApi().createMailBox("Nickseven123","Hahahaha")

for mail in mails:
    mail.sendBack("abcsdf","")