#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from pelicanconf import *

SITEURL = 'http://192.168.44.58:8100'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Uncomment following line for absolute URLs in production:
RELATIVE_URLS = False

DISQUS_SITENAME = "xrpblog"
GITHUB_URL = "http://github.com/HorizonXP"
TWITTER_USERNAME = "xitijpatel"
HNSHARE_ENABLED = True
GOOGLE_ANALYTICS = "UA-6342364-2"
GITHUB_ACTIVITY_FEED = 'https://github.com/HorizonXP.atom'
