#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at Jul 16 16:59 by BlahGeek@Gmail.com

import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

import subprocess
import os

CMD = ['/home/blahgeek/sites/treehole/manage.py', 'whois']

def predict(text):
    return text.startswith('treehole')

def handle(text):
    num = text.replace('treehole', '').strip()
    backup = os.environ.get('DJANGO_SETTINGS_MODULE', '')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'treehole.settings'
    ret = subprocess.check_output(CMD + [str(num)])
    os.environ['DJANGO_SETTINGS_MODULE'] = backup
    return ret
