#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by i@BlahGeek.com at 2015-01-18

from . import Plugin
import requests
import re

class YOURLSPlugin(Plugin):

    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    signature = 'f4531f65ca'
    url = 'http://blaa.ml/s/yourls-api.php'

    def predict(self, text):
        if self.regex.match(text):
            return 90
        return 0

    def handle(self, text, userid):
        try:
            r = requests.get(self.url, params={
                                'action': 'shorturl',
                                'signature': self.signature,
                                'url': text,
                                'format': 'json'
                             }, timeout=5).json()
            if not 'shorturl' in r:
                return 'Failed! Not a valid URL?'
            details = r.get('url', {})
            return '%s -> %s' % (r['shorturl'],
                                 details.get('url'))
        except requests.Timeout:
            return 'Timeout'
