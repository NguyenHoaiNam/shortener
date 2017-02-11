#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

# using sqlite as database
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/app.db'
# log level
LOG_LEVEL = 'INFO'
# log file
LOG_FILE = '/tmp/shortener.log'
# Rate limit. Syntax should follow goo.gl/FWxPrF
RATE_LIMIT = '200/hour;15/minute'

