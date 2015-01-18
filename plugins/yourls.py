#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by i@BlahGeek.com at 2015-01-18

from . import Plugin
import requests

class YOURLSPlugin(Plugin):

    target = None

    signature = 'f4531f65ca'
    url = 'http://blaa.ml/s/yourls-api.php'

    def predict(self, text):
        action, _, self.target = text.strip().partition(' ')
        if action == 'short' and len(self.target) > 0:
            return 100
        return 0

    def handle(self, text, userid):
        try:
            r = requests.get(self.url, params={
                                'action': 'shorturl',
                                'signature': self.signature,
                                'url': self.target,
                                'format': 'json'
                             }, timeout=5).json()
            if not 'shorturl' in r:
                return 'Failed! Not a valid URL?'
            details = r.get('url', {})
            return '%s -> %s (%s)' % (r['shorturl'],
                                      details.get('url'),
                                      details.get('title'))
        except requests.Timeout:
            return 'Timeout'
