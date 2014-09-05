#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by i@BlahGeek.com at 2014-04-20


class PluginMeta(type):

    def __init__(cls, name, bases, attrs):
        super(PluginMeta, cls).__init__(name, bases, attrs)
        if not hasattr(cls, '_plugins'):
            cls._plugins = set()
        cls._plugins.add(cls)
        cls._plugins -= set(bases)

    __iter__ = lambda cls: iter(cls._plugins)


class Plugin(object):
    ''' Plugin base class '''

    __metaclass__ = PluginMeta

    def predict(self, text):
        ''' @text: unicode
            return: 0 - 100 '''
        raise NotImplementedError()

    def handle(self, text, userid):
        ''' @text: unicode
            return unicode '''
        raise NotImplementedError()

__all__ = ['sample', 'keywordreplyplugin', 'voteplugin']
