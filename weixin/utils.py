#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at May 03 13:36 by BlahGeek@Gmail.com

from weixin.settings import WEIXIN_TOKEN
import hashlib
import xml.etree.ElementTree as ET

def checkSig(req):
    signature = req.GET.get("signature", '')
    timestamp = req.GET.get("timestamp", '')
    nonce = req.GET.get("nonce", '')
    tmp = ''.join(sorted([WEIXIN_TOKEN, timestamp, nonce]))
    tmp = hashlib.sha1(tmp).hexdigest()
    return tmp == signature

def parseXml(req):
    xml_tree = ET.fromstring(req.body)
    content = dict()
    for i in xml_tree:
        content[i.tag] = i.text
    return content

def makeXml(dic, root_tag = 'xml'):
    xml_tree = ET.Element(root_tag)
    def _make_node(root, key, val):
        if type(val) == ET.Element:
            root.append(val)
            return
        node = ET.SubElement(root, key)
        if type(val) == str or type(val) == unicode:
            node.text = val
        elif type(val) == dict:
            for i in val:
                _make_node(node, i, val[i])
    for i in dic:
        _make_node(xml_tree, i, dic[i])
    return xml_tree
#    return ET.tostring(xml_tree)
