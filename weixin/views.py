#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at May 03 12:43 by BlahGeek@Gmail.com

import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib import messages
from weixin.settings import WEIXIN_TOKEN
import hashlib

def checkSig(req):
    signature = req.GET.get("signature", None)
    timestamp = req.GET.get("timestamp", None)
    nonce = req.GET.get("nonce", None)
    echoStr = req.GET.get("echostr", None)
    tmp = ''.join(sorted([WEIXIN_TOKEN, timestamp, nonce]))
    tmp = hashlib.sha1(tmp).hexdigest()
    return echoStr if tmp == signature else ''

def index(req):
    if req.method == 'GET':
        return HttpResponse(checkSig(req))
    else:
        return HttpResponse('')
