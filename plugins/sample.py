#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by i@BlahGeek.com at 2014-04-12

from . import Plugin


class SamplePlugin(Plugin):

    def predict(self, text):
        ''' text: unicode
            return: number, 0-100 '''
        return 10

    def handle(self, text, userid):
        ''' return unicode '''
        return 'I got: %s from %s, Yeah!' % (text, userid)
