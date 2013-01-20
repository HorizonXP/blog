#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Xitij Ritesh Patel'
SITENAME = u"Xitij Ritesh Patel"
SITEURL = 'http://www.xitijpatel.com'
THEME = "xrpblog"

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = u'en'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
TYPOGRIFY = True
PATH = 'content'
STATIC_PATHS = ['images', 'other_files',]
OUTPUT_PATH = 'output'

FEED_DOMAIN=SITEURL
FEED_ALL_RSS="feeds/all.rss.xml"

# Blogroll
LINKS =  (('Pulsecode Engineering', 'http://pulsecode.ca'),
          ('taab', 'http://taab.co'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/xitijpatel'),
        ('Facebook', 'http://facebook.com/xpatel'),)

DEFAULT_PAGINATION = False
