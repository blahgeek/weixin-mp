#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at May 03 12:43 by BlahGeek@Gmail.com

import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.http import require_http_methods
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib import messages
from .utils import *
from .messages import *
from calendar.sample import getTodayEvents, getTomorrowEvents

def index(req):
    if not checkSig(req):
        return HttpResponseForbidden()
    if req.method == 'GET':
        return HttpResponse(req.GET.get('echostr', ''))
    req_msg = parseXml(req)
    ret = u''

    if req_msg.get('MsgType', '') == 'text':
        text = req_msg.get('Content', '')
        if u'亲爱' in text and u'有空' in text:
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

    return HttpResponse(makeTextMsg(req_msg, ret))
