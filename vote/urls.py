#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by i@BlahGeek.com at 2014-09-05

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^getjson/$', 'vote.views.getJson', name='vote.getjson'),
    url(r'^$', 'vote.views.index', name='vote.index'),
)
