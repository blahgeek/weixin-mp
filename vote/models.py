#!/usr/bin/env python2
# -*- coding=UTF-8 -*-

from django.db import models
from solo.models import SingletonModel


class VoteConfiguration(SingletonModel):

    def __unicode__(self):
        return 'Vote Configuration'

    vote_name = models.CharField(max_length=255, default='4th IDEA Challenge',
        help_text='Vote title')
    max_vote_per_user = models.IntegerField(default=3, 
        help_text='Max votes a user can submit')
    candidate_number = models.IntegerField(default=10,
        help_text='How many candidate do we have?')
    prefix = models.CharField(max_length=255, default=u'投票',
        help_text='Prefix for votes for detecting')

    fail_msg = models.TextField(default=u'投票失败！投票格式：“投票 3 4 5”，最多可投3个不同的作品，作品范围为1-10',
        help_text='Fail message')
    dup_msg = models.TextField(default=u'投票失败！您已投过！',
        help_text='Fail message for duplicate')
    ok_msg = models.TextField(default=u'投票成功！',
        help_text='Success message')


class VoteModel(models.Model):
    candidate = models.IntegerField(db_index=True)
    count = models.IntegerField(default=0)

class VotedUserModel(models.Model):
    userid = models.CharField(db_index=True, max_length=1024)
