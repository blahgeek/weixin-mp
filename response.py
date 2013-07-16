#!/usr/bin/env python2
# -*- coding=UTF-8 -*-
# Created at Jul 16 15:59 by BlahGeek@Gmail.com

import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

import os
import imp
FILE_DIR = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.join(FILE_DIR, 'lib'))
PLUGIN_DIR = os.path.join(FILE_DIR, 'plugins')

_files = os.listdir(PLUGIN_DIR)
_files = filter(lambda x: x.endswith('.py'), _files)
plugins = map(lambda x: imp.load_source('', os.path.join(PLUGIN_DIR, x)), _files)

def response(text):
    try:
        plugin = filter(lambda x: x.predict(text), plugins)[0]
    except IndexError:
        print >> sys.stderr, 'None available'
        return ''
    print >> sys.stderr, 'Handle using', plugin
    return plugin.handle(text)

if __name__ == '__main__':
    print response(sys.argv[1].decode('utf8'))
