# -*- coding: utf-8 -*-

import httplib2
import os
import sys
from dateutil.parser import parse
from datetime import datetime, timedelta

try:
    from .apiclient.discovery import build
except ValueError:
    from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run

TIMEZONE = '+08:00'  # It's a quick hack, FIXME

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
CLIENT_SECRETS = os.path.join(DIR_PATH, 'client_secrets.json')

FLOW = flow_from_clientsecrets(CLIENT_SECRETS,
        scope=[
            'https://www.googleapis.com/auth/calendar.readonly', 
            ])

def parseTime(t):
    t = t.strip().replace(TIMEZONE, '')
    return parse(t)

def getEvents(start, end):
    storage = Storage(os.path.join(DIR_PATH, 'sample.dat'))
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
            timeMin=start.isoformat()+TIMEZONE, 
            timeMax=end.isoformat()+TIMEZONE, )

    response = request.execute()
    return [(x['summary'], x.get('location', ''), \
        parseTime(x['start']['dateTime']), parseTime(x['end']['dateTime']))\
            for x in response.get('items', [])]

def getTodayEvents():
    now = datetime.now()
    end = datetime(year=now.year, month=now.month, day=now.day, 
                   hour=23, minute=59, second=59)
    return getEvents(now, end)

def getTomorrowEvents():
    tomorrow_now = datetime.now() + timedelta(days=1)
    start = datetime(year=tomorrow_now.year, month=tomorrow_now.month, day=tomorrow_now.day, 
                   hour=0, minute=0, second=1)
    return getEvents(start, start + timedelta(days=1))

if __name__ == '__main__':
    for x in getTodayEvents():
        print x
