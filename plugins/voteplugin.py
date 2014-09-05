#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by i@BlahGeek.com at 2014-09-05

from . import Plugin
from vote.models import VoteModel, VoteConfiguration, VotedUserModel


class VotePlugin(Plugin):

    def __init__(self):
        self.conf = VoteConfiguration.objects.get()
        self.prefix = self.conf.prefix

    def predict(self, text):
        if text.strip().startswith(self.prefix):
            return 100
        else:
            return 0

    def handle(self, text, userid):
        if VotedUserModel.objects.filter(userid=userid).count() > 0:
            return self.conf.dup_msg
        numbers = text.strip().split(' ')[1:]
        numbers = filter(lambda x: len(x.strip()), numbers)
        try:
            numbers = map(int, numbers)
        except ValueError:
            return self.conf.fail_msg
        if len(set(numbers)) != len(numbers) or \
                len(numbers) > self.conf.max_vote_per_user or \
                len(numbers) == 0:
            return self.conf.fail_msg
        for x in numbers:
            if x <= 0 or x > self.conf.candidate_number:
                return self.conf.fail_msg
        usermodel = VotedUserModel(userid=userid)
        usermodel.save()

        for x in numbers:
            try:
                model = VoteModel.objects.get(candidate=x)
            except VoteModel.DoesNotExist:
                model = VoteModel(candidate=x)
            model.count += 1
            model.save()

        return self.conf.ok_msg
