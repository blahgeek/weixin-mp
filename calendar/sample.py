# -*- coding: utf-8 -*-

import httplib2
import os
import sys
from dateutil.parser import parse
from datetime import datetime, timedelta

try:
    from .apiclient.discovery import build
except ImportError:
    from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run

TIMEZONE = '+08:00'  # It's a quick hack, FIXME

CLIENT_SECRETS = os.path.join(os.path.dirname(\
        os.path.realpath(__file__)), 'client_secrets.json')

FLOW = flow_from_clientsecrets(CLIENT_SECRETS,
        scope=[
            'https://www.googleapis.com/auth/calendar.readonly', 
            ])

def parseTime(t):
    t = t.strip().replace(TIMEZONE, '')
    return parse(t)

def getRecentEvent(delta):
    storage = Storage('sample.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = run(FLOW, storage)
    http = httplib2.Http()
    http = credentials.authorize(http)

    service = build('calendar', 'v3', http=http)

    request = service.events().list(
            calendarId='primary', 
            singleEvents=True, 
            orderBy='startTime', 
            timeMin=datetime.now().isoformat()+TIMEZONE, 
            timeMax=(datetime.now()+delta).isoformat()+TIMEZONE, )

    response = request.execute()
    return [(x['summary'], parseTime(x['start']['dateTime']), parseTime(x['end']['dateTime']))\
            for x in response.get('items', [])]

if __name__ == '__main__':
    delta = timedelta(days=1)
    for x in getRecentEvent(delta):
        print x[0], (x[1] - datetime.now()).total_seconds(), (x[2] - datetime.now()).total_seconds()
