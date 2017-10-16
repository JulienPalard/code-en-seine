#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Julien Palard'
SITENAME = 'Code-en-Seine'
SITEURL = 'https://codeenseine.fr'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'

CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'https://blog.getpelican.com/'),
         ('Python.org', 'https://python.org/'))



# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/code_en_seine'),)

DEFAULT_PAGINATION = 10

THEME = 'theme'
THEME_STATIC_DIR = 'theme'
STATIC_PATHS = ['images']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
