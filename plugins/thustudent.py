#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by i@BlahGeek.com at 2014-10-11

import sqlite3
from . import Plugin
import os
import re

path = os.path.dirname(__file__)
path = os.path.join(path, 'student.sqlite3')

class THUStudentPlugin(Plugin):

    def predict(self, text):
        if text.endswith(u'是谁'):
            self.name = re.sub(u'是谁$', '', text)
            return 90
        if text.startswith(u'谁是'):
            self.name = re.sub(u'^谁是', '', text)
            return 90
        return 0

    def make_str(self, data):
        ret = '%s(%s,%s)' % (data[1], data[0], data[7])
        ret += u'，' + data[2] + u'，' + (data[5] if data[6] is None else data[6])
        ret += u'，' + '%s(%s)' % (data[4], data[3])
        ret += u'，身份证' + data[8]
        if data[9] and data[9] != 'NULL':
            ret += u'，邮箱' + data[9]
        if data[10] and data[10] != 'NULL':
            ret += u'，人人' + data[10]
        return ret

    def handle(self, text, userid):
        conn = sqlite3.connect(path)
        cursor = conn.cursor()

        name = self.name.strip()
        if name.startswith('2'):
            cursor.execute('select * from student where id = ?', (name, ))
        else:
            cursor.execute('select * from student where name = ?', (name, ))
        results = cursor.fetchall()
        if not results:
            return u'未找到结果！'
        elif len(results) == 1:
            return self.make_str(results[0])
        else:
            return u'多个结果：' + u'，'.join([x[0] for x in results])
