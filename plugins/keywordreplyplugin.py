#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by i@BlahGeek.com at 2014-09-05

from . import Plugin
from keywordreply.models import KeywordReplyModel

class KeywordReplyPlugin(Plugin):

    reply = None

    def predict(self, text):
        text = text.strip()
        try:
            self.reply = KeywordReplyModel.objects.filter(keyword=text).order_by('?')[0]
        except IndexError:
            self.reply = None
            return 0
        return 50

    def handle(self, text, userid):
        assert self.reply is not None
        self.reply.count += 1
        self.reply.save()
        return self.reply.reply
