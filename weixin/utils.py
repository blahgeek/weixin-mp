#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at May 03 13:36 by BlahGeek@Gmail.com

import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

from weixin.settings import WEIXIN_TOKEN
import hashlib
import xml.etree.ElementTree as ET

def checkSig(req):
    signature = req.GET.get("signature", None)
    timestamp = req.GET.get("timestamp", None)
    nonce = req.GET.get("nonce", None)
    tmp = ''.join(sorted([WEIXIN_TOKEN, timestamp, nonce]))
    tmp = hashlib.sha1(tmp).hexdigest()
    return tmp == signature

def parseXml(req):
    xml_tree = ET.fromstring(req.body)
    content = dict()
    for i in xml_tree:
        content[i.tag] = i.text
    return content

def makeXml(dic):
    xml_tree = ET.Element('xml')
    for i in dic:
        tmp = ET.SubElement(xml_tree, i)
        tmp.text = dic[i]
    return ET.tostring(xml_tree)
