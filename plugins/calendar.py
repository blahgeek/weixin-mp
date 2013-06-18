#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at Jun 18 22:32 by BlahGeek@Gmail.com

import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

from plugins.cal.sample import getTodayEvents, getTomorrowEvents

def canHandle(text):
    return True if u'有空' in text and \
            (u'今天' in text or u'明天' in text) else False


def handle(text):
    ret = u''
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
