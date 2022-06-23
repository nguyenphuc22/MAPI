import Gmail
from Factory import Factory
import imaplib
import email
import traceback

class FactoryGmail(Factory):
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def createMailBox(self) -> list:
        FROM_EMAIL = self.username
        FROM_PWD = self.password
        SMTP_SERVER = "imap.gmail.com"
        SMTP_PORT = 993
        emails = list()

        try:
            mail = imaplib.IMAP4_SSL(SMTP_SERVER)
            mail.login(FROM_EMAIL, FROM_PWD)
            mail.select('inbox')

            data = mail.search(None, '(UNSEEN)')
            print(data)
            mail_ids = data[1]
            id_list = mail_ids[0].split()

            for i in id_list:
                print(i)
                data = mail.fetch(str(int(i)), '(RFC822)')
                for response_part in data:
                    arr = response_part[0]
                    if isinstance(arr, tuple):
                        msg = email.message_from_string(str(arr[1], 'utf-8'))
                        emails.append(Gmail.Gmail(msg,False,FROM_EMAIL,FROM_PWD))

        except Exception as e:
            traceback.print_exc()

        return emails