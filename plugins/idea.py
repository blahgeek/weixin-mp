#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by i@BlahGeek.com at 2014-04-07

import subprocess
import os

CMD = ['/home/blahgeek/sites/idea.challenge/venv/bin/python2', 
       '/home/blahgeek/sites/idea.challenge/manage.py', 'box']

def predict(text):
    return text.startswith('box')

def handle(text):
    args = text.replace('box', '').strip().split(' ')
    backup = os.environ.get('DJANGO_SETTINGS_MODULE', '')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'challenge.settings'
    ret = subprocess.check_output(CMD + args)
    os.environ['DJANGO_SETTINGS_MODULE'] = backup
    return ret.decode('utf8')
