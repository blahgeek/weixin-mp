#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at May 03 12:43 by BlahGeek@Gmail.com

from django.http import HttpResponse, HttpResponseForbidden
from .utils import checkSig, parseXml
from .messages import makeTextMsg
from response import response
from msg import NULL_RESPONSE

def index(req):
    if not checkSig(req):
        return HttpResponseForbidden()
    if req.method == 'GET':
        return HttpResponse(req.GET.get('echostr', ''))
    req_msg = parseXml(req)
    ret = NULL_RESPONSE

    if req_msg.get('MsgType', '') == 'text':
        ret = response(req_msg.get('Content', ''))

    return HttpResponse(makeTextMsg(req_msg, ret))
