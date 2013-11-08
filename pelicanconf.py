#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pelicanconf import *


AUTHOR = u"Ross O'Brien"
SITENAME = u'Ross O\'Brien'
SITEURL = 'http://local.obrienross.com'
SITESUBTITLE = "Web Developer - Seattle, WA"

TIMEZONE = 'USA/Los Angeles'

DEFAULT_DATE_FORMAT = ('%B %d, %Y')

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

SUMMARY_MAX_LENGTH = 100

THEME = "/home/ross/workspace/red-block/"

# Blogroll
LINKS =  ()

MENUITEMS = (('Work', 'A brief overview of my personal projects and work experience', '/pages/work.html'),
			 ('About', 'Hi! I\'m Ross. I build websites.', '/pages/about.html'),
			 ('Blog', 'Thoughs on random things.', '/'),
			 ('Contact', 'Get in touch!', '/pages/contact.html'))

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/obrienross'),
          ('github', 'http://github.com/rossobrien'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
