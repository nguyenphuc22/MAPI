from email import encoders
from email.mime.base import MIMEBase
from email import encoders
from email.mime.base import MIMEBase

from EmailInterface import EmailInterface
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Gmail(EmailInterface):

    def __init__(self,msg,state,username,password):
        self.email = msg
        self.isSeen = state
        self.mUsername = username
        self.mPassword = password

    def isValidate(self) -> bool:
        return super().isValidate()

    def getSubject(self) -> str:
        return self.email['subject']

    def getBody(self) -> str:
        self.isSeen = True
        if self.email.is_multipart():
            mail_content = ''

            # on multipart we have the text message and
            # another things like annex, and html version
            # of the message, in that case we loop through
            # the email payload
            for part in self.email.get_payload():
                # if the content type is text/plain
                # we extract it
                if part.get_content_type() == 'text/plain':
                    mail_content += part.get_payload()
        else:
            # if the message isn't multipart, just extract it
            mail_content = self.email.get_payload()

        return mail_content

    def getUnRead(self) -> bool:
        return self.isSeen

    def getSender(self) -> str:
        return self.email['from']

    def sendBack(self, body, path):

        receiver_email = self.email['from']

        sender_email = self.mUsername
        password = self.mPassword

        message = MIMEMultipart("alternative")
        message["Subject"] = "I'm Bot"

        message["From"] = sender_email
        message["To"] = receiver_email

        part1 = MIMEText(body, "plain")

        message.attach(part1)

        if path:
            with open(path, "rb") as attachment:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

                encoders.encode_base64(part)

                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {path}",
                )

                message.attach(part)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

from EmailInterface import EmailInterface
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Gmail(EmailInterface):

    def __init__(self,msg,state,username,password):
        self.email = msg
        self.isSeen = state
        self.mUsername = username
        self.mPassword = password

    def isValidate(self) -> bool:
        return super().isValidate()

    def getSubject(self) -> str:
        return self.email['subject']

    def getBody(self) -> str:
        self.isSeen = True
        if self.email.is_multipart():
            mail_content = ''

            # on multipart we have the text message and
            # another things like annex, and html version
            # of the message, in that case we loop through
            # the email payload
            for part in self.email.get_payload():
                # if the content type is text/plain
                # we extract it
                if part.get_content_type() == 'text/plain':
                    mail_content += part.get_payload()
        else:
            # if the message isn't multipart, just extract it
            mail_content = self.email.get_payload()

        return mail_content

    def getUnRead(self) -> bool:
        return self.isSeen

    def getSender(self) -> str:
        return self.email['from']

    def sendBack(self, body, path):

        receiver_email = self.email['from']

        sender_email = self.mUsername
        password = self.mPassword

        message = MIMEMultipart("alternative")
        message["Subject"] = "I'm Bot"

        message["From"] = sender_email
        message["To"] = receiver_email

        part1 = MIMEText(body, "plain")

        message.attach(part1)

        if path:
            with open(path, "rb") as attachment:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

                encoders.encode_base64(part)

                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {path}",
                )

                message.attach(part)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
