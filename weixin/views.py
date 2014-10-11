#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at May 03 12:43 by BlahGeek@Gmail.com

from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from .utils import checkSig, parseXml
from .messages import makeTextMsg, makeImageMsg
from response import response
from msg import NULL_RESPONSE

@csrf_exempt
def index(req):
    if not checkSig(req):
        return HttpResponseForbidden()
    if req.method == 'GET':
        return HttpResponse(req.GET.get('echostr', ''))
    req_msg = parseXml(req)
    ret = NULL_RESPONSE

    if req_msg.get('MsgType', '') == 'text':
        ret = response(req_msg.get('Content', ''), req_msg['FromUserName'])

    if isinstance(ret, unicode) or isinstance(ret, str):
        ret = makeTextMsg(req_msg, ret)
    elif isinstance(ret, list) or isinstance(ret, tuple):
        ret = makeImageMsg(req_msg, ret)

    return HttpResponse(ret)
