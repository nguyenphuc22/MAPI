from __future__ import print_function

import GmailApi
from Factory import Factory

import base64
import os.path

from bs4 import BeautifulSoup
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://mail.google.com/']

class FactoryGmailApi(Factory):

    def createMailBox(self, username, password) -> list:
        """Shows basic usage of the Gmail API.
            Lists the user's Gmail labels.
            """
        emails = list()
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'client.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            # Call the Gmail API
            service = build('gmail', 'v1', credentials=creds)

            results = service.users().messages().list(userId='me', labelIds=['UNREAD']).execute()

            messages = results.get('messages', [])

            if not messages:
                print("No messages found.")
            else:
                for message in messages:
                    modify = service.users().messages().modify(userId='me', id=message['id'],
                                                               body={"removeLabelIds": ['UNREAD']}).execute()
                    msg = service.users().messages().get(userId='me', id=message['id']).execute()
                    emails.append(GmailApi.GmailApi(service= service,message= msg))

        except HttpError as error:
            # TODO(developer) - Handle errors from gmail API.
            print(f'An error occurred: {error}')

        return emails