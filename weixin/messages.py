#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at May 03 13:37 by BlahGeek@Gmail.com

import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

import time
from .utils import makeXml

def makeMsg(req_msg, dic):
    dic.update({
        'ToUserName': req_msg['FromUserName'], 
        'FromUserName': req_msg['ToUserName'], 
        'CreateTime': int(time.time()), 
        'FuncFlag': '0', 
        })
    return makeXml(dic)

def makeTextMsg(req_msg, text):
    return makeMsg(req_msg, {
        'MsgType': 'text', 
        'Content': text, 
        })

def makeMusicMsg(req_msg, url, hqurl = None):
    return makeMsg(req_msg, {
        'MsgType': 'music', 
        'MusicUrl': url, 
        'HQMusicUrl': hqurl if hqurl else url, 
        })

