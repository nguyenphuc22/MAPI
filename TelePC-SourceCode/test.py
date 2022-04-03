import MailBox

mailBox = MailBox.MailBox()
mails = mailBox.getUnreadMails()
for mail in mails :
    print(mail.getBody())