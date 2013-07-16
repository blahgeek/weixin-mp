#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at Jul 16 15:18 by BlahGeek@Gmail.com

import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

import httplib2
import os
from dateutil.parser import parse
from datetime import datetime, timedelta

from lib.apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run

TIMEZONE = '+08:00'  # It's a quick hack, FIXME

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DIR_PATH = os.path.join(DIR_PATH, 'calendar_data')
CLIENT_SECRETS = os.path.join(DIR_PATH, 'client_secrets.json')

FLOW = flow_from_clientsecrets(CLIENT_SECRETS,
        scope=[
            'https://www.googleapis.com/auth/calendar.readonly', 
            ])

def parseTime(t):
    t = t.strip().replace(TIMEZONE, '')
    return parse(t)

def getEvents(start, end):
    storage = Storage(os.path.join(DIR_PATH, 'storage.dat'))
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

def predict(text):
    return u'有空' in text

def handle(text):
    ret = ''
    events = None
    if u'今天' in text:
        events = getTodayEvents()
    elif u'明天' in text:
        events = getTomorrowEvents()

    if events is None:
        ret = u'我是机器人，理解不了了耶，直接来找我问啦...'
    elif len(events) == 0:
        ret = u'似乎没有事耶 :P'
    else:
        for x in events:
            ret += x[2].strftime('%H:%M') + '-'
            ret += x[3].strftime('%H:%M')
            if x[1] != '':
                ret += u'在' + x[1]
            ret += u'有' + x[0] + u'; '
    return ret

if __name__ == '__main__':
    for x in getTodayEvents():
        print x

