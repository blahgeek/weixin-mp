#!/usr/bin/env python
# -*- coding=UTF-8 -*-

from django.db import models

# Create your models here.

class ImageReplyModel(models.Model):
    title = models.TextField(help_text='Message title')
    description = models.TextField(help_text='Message description')
    picurl = models.CharField(max_length=1024, 
        help_text=u'图片链接，支持JPG、PNG格式，较好的效果为大图360*200，小图200*200')
    url = models.CharField(max_length=1024, 
        help_text=u'点击图文消息跳转链接')

    def __unicode__(self):
        return self.title



class KeywordReplyModel(models.Model):
    keyword = models.CharField(max_length=255, help_text="Keyword for match", db_index=True)
    reply = models.TextField(help_text=u"回复的文本消息，如果下面的图文消息被选中，则该项被忽略")
    count = models.IntegerField(default=0, editable=False,
        help_text="How many times this keyword was matched, it's automaticlly counted")

    imagereply = models.ManyToManyField(ImageReplyModel)

    def __unicode__(self):
        return 'Keyword: %s; Match Count: %d' % (self.keyword, self.count)

