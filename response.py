#!/usr/bin/env python2
# -*- coding=UTF-8 -*-
# Created at Jul 16 15:59 by BlahGeek@Gmail.com

import sys
import os
import imp
import logging
from msg import NO_HANDLER

FILE_DIR = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.join(FILE_DIR, 'lib'))
PLUGIN_DIR = os.path.join(FILE_DIR, 'plugins')

plugins = []

files = filter(lambda x: x.endswith('.py'), os.listdir(PLUGIN_DIR))
files = map(lambda x: x.replace('.py', ''), files)

for x in files:
    name = x.replace('.py', '')
    fp, pathname, desc = imp.find_module(name, [PLUGIN_DIR])
    plugins.append(imp.load_module(name, fp, pathname, desc))

plugins = filter(lambda m: hasattr(m, 'predict') and hasattr(m, 'handle'), plugins)


def response(text):
    try:
        plugin = max(plugins, key=lambda x: x.predict(text))
    except ValueError:
        logging.warn('No handler available.')
        return NO_HANDLER
    logging.info('Using handler: %s' % str(plugin))
    return plugin.handle(text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    print response(sys.argv[1].decode('utf8'))
