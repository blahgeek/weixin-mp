#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by i@BlahGeek.com at 2014-11-06

from . import Plugin
import requests
import random

class DormLightPlugin(Plugin):

    action = None

    replys = (u'哦', u'嗯', u'好…', u'好了…',)

    ON_URL = 'http://dorm.blahgeek.com:4242/turnon505A'
    OFF_URL = 'http://dorm.blahgeek.com:4242/turnoff505A'

    def predict(self, text):
        if text == u'求开灯':
            self.action = True
            return 100
        if text == u'求关灯':
            self.action = False
            return 100
        return 0

    def handle(self, text, userid):
        try:
            requests.get(self.ON_URL if self.action else self.OFF_URL, 
                         allow_redirects=False,
                         timeout=3)
        except requests.Timeout:
            return 'Timeout'
        return random.choice(self.replys)

