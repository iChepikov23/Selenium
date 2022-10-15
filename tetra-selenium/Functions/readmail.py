from __future__ import print_function

import base64
import datetime
import email
import os.path
import time

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def read_mail():
    directory = os.path.dirname(__file__)
    directory = directory.replace('Functions', 'data')
    credentials = os.path.join(os.path.sep, directory, 'credentials.json')
    token = os.path.join(os.path.sep, directory, 'token.json')
    credentials = None

    if os.path.exists(token):
        credentials = Credentials.from_authorized_user_file(token, SCOPES)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials, SCOPES)
            credentials = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token, 'w') as token:
            token.write(credentials.to_json())

    service = build('gmail', 'v1', credentials=credentials)

    epoch_time = int(time.time())

    after_10_minutes = (datetime.datetime.now() - datetime.timedelta(minutes=1))
    after = int(time.mktime(after_10_minutes.timetuple()))
    # request a list of all the messages
    var = 'newer_than:1d has invited you to join their team after:' + str(after)
    result = service.users().messages().list(userId='me', q=var).execute()

    # We can also pass maxResults to get any number of emails. Like this:
    # result = service.users().messages().list(maxResults=200, userId='me').execute()
    messages = result.get('messages')
    link = None
    if not messages:
        link = None
    else:
        for message in messages:
            content = service.users().messages().get(userId='me', id=message['id']).execute()

            if "data" in content['payload']['body']:
                message = content['payload']['body']['data']
                message = data_encoder(message)
                for line in str(message).splitlines():
                    if line.index('access_token'):
                        link = line.replace('app', 'staging')
            elif "data" in content['payload']['parts'][0]['body']:
                message = content['payload']['parts'][0]['body']['data']
                # in this message find link to confirm
                message = data_encoder(message)
                for line in str(message).splitlines():
                    if line.find('access_token') >= 0:
                        link = line.replace('app', 'staging')
            else:
                print("body has no data.")
            break

    return link


def read_confirm_mail():
    directory = os.path.dirname(__file__)
    directory = directory.replace('Functions', 'data')
    credentials = os.path.join(os.path.sep, directory, 'credentials.json')
    token = os.path.join(os.path.sep, directory, 'token.json')
    credentials = None

    if os.path.exists(token):
        credentials = Credentials.from_authorized_user_file(token, SCOPES)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials, SCOPES)
            credentials = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token, 'w') as token:
            token.write(credentials.to_json())

    service = build('gmail', 'v1', credentials=credentials)

    epoch_time = int(time.time())

    after_10_minutes = (datetime.datetime.now() - datetime.timedelta(seconds=5))
    after = int(time.mktime(after_10_minutes.timetuple()))
    # request a list of all the messages

    var = 'newer_than:1d Verify email address after:' + str(after)
    result = service.users().messages().list(userId='me', q=var).execute()

    # We can also pass maxResults to get any number of emails. Like this:
    # result = service.users().messages().list(maxResults=200, userId='me').execute()
    messages = result.get('messages')
    link = None
    if not messages:
        link = None
    else:
        for message in messages:
            content = service.users().messages().get(userId='me', id=message['id']).execute()
            if "data" in content['payload']['body']:
                message = content['payload']['body']['data']
                message = str(data_encoder(message))
                if message.find('href') >= 0:
                    index = message.find('href')
                    link = message[index + 6: int(message.find('">', index))]
                    break
            elif "data" in content['payload']['parts'][0]['body']:
                message = content['payload']['parts'][0]['body']['data']
                # in this message find link to confirm
                message = str(data_encoder(message))
                if message.find('href') >= 0:
                    index = message.find('href')
                    link = message[index + 6: int(message.find('">', index))]
                    break
            else:
                print("body has no data.")
            break

    return link


def read_two_step_mail():
    directory = os.path.dirname(__file__)
    directory = directory.replace('Functions', 'data')
    credentials = os.path.join(os.path.sep, directory, 'credentials.json')
    token = os.path.join(os.path.sep, directory, 'token.json')
    credentials = None

    if os.path.exists(token):
        credentials = Credentials.from_authorized_user_file(token, SCOPES)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials, SCOPES)
            credentials = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token, 'w') as token:
            token.write(credentials.to_json())

    service = build('gmail', 'v1', credentials=credentials)
    epoch_time = int(time.time())
    after_10_minutes = (datetime.datetime.now() - datetime.timedelta(seconds=20))
    after = int(time.mktime(after_10_minutes.timetuple()))
    # request a list of all the messages
    var = 'newer_than:1d Authentication Code after:' + str(after)
    result = service.users().messages().list(userId='me', q=var).execute()
    # We can also pass maxResults to get any number of emails. Like this:
    # result = service.users().messages().list(maxResults=200, userId='me').execute()
    messages = result.get('messages')
    link = None
    if not messages:
        link = None
    else:
        for message in messages:
            content = service.users().messages().get(userId='me', id=message['id']).execute()

            if "data" in content['payload']['body']:
                message = content['payload']['body']['data']
                message = str(data_encoder(message))
                if message.find('<h3 style="margin: 0">') >= 0:
                    index = message.find('<h3 style="margin: 0">')
                    index_c = message.index('>', index)
                    index_h = message.index('<', index + 3)
                    link = message[index_c + 1:index_h]
            elif "data" in content['payload']['parts'][0]['body']:
                message = content['payload']['parts'][0]['body']['data']
                # in this message find link to confirm
                message = str(data_encoder(message))
                if message.find('<h3 style="margin: 0">') >= 0:
                    index = message.find('<h3 style="margin: 0">')
                    index_c = message.index('>', index)
                    index_h = message.index('<', index + 3)
                    link = message[index_c + 1:index_h]
            else:
                print("body has no data.")
            break

    return link


def data_encoder(text):
    if len(text) > 0:
        message = base64.urlsafe_b64decode(text)
        message = str(message, 'utf-8')
        message = email.message_from_string(message)
        return message
