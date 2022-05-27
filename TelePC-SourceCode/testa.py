import FactoryGmailApi

mails  = FactoryGmailApi.FactoryGmailApi().createMailBox("nguyenphuc2201001@gmail.com","Khutaosong21")

for mail in mails:
    mail.getBody()