#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at Jul 16 16:59 by BlahGeek@Gmail.com

import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

import sqlite3

DB_FILE = os.path.join(os.path.dirname(__file__), 'student.sqlite3')

def predict(text):
    return text.startswith('search')

def handle(text):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    text = text.replace('search', '').strip()
    text = text.split(' ')
    if text[0] in ('name', 'id', 'username', 'pid'):
        c.execute("select * from student where %s = ?" % text[0], [text[1]])
    if text[0] == 'ip':
        c.execute("select * from ip where ip = ?", [text[1]])
    ret = map(lambda x: [i for i in x if i is not None], c.fetchall())
    return '; '.join([','.join(x) for x in ret])
