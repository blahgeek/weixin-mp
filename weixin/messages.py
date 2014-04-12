#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at May 03 13:37 by BlahGeek@Gmail.com

import time
import xml.etree.ElementTree as ET
from .utils import makeXml

def makeMsg(req_msg, dic):
    dic.update({
        'ToUserName': req_msg['FromUserName'], 
        'FromUserName': req_msg['ToUserName'], 
        'CreateTime': str(int(time.time())), 
        'FuncFlag': '0', 
        })
    return ET.tostring(makeXml(dic), 'utf8')

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

def makeImageMsg(req_msg, images):
    # images := ((picurl, title, desc, url), ...)
    articles = ET.Element('Articles')
    for i in images:
        articles.append(makeXml({
            'PicUrl': i[0], 
            'Title': i[1], 
            'Description': i[2], 
            'Url': i[3]}, 'item'))
    return makeMsg(req_msg, {
        'MsgType': 'news', 
        'ArticleCount': str(len(images)), 
        'Articles': articles, 
        })
