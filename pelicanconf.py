#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pelicanconf import *

AUTHOR = u"Ross O'Brien"
SITENAME = u'Ross O\'Brien'
SITEURL = 'http://local.obrienross.com'
SITESUBTITLE = "Web Developer - Seattle, WA"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_DATE_FORMAT = ('%B %d, %Y')

DEFAULT_LANG = u'en'

SUMMARY_MAX_LENGTH = 100

THEME = "./theme/"

MENUITEMS = (('Work', 'A brief overview of my personal projects and work experience', '/pages/work.html'),
			 ('About', 'Hi! I\'m Ross. I build websites.', '/pages/about.html'),
			 ('Blog', 'Thoughs on random things.', '/index.html'),
			 ('Contact', 'Get in touch!', '/pages/contact.html'))

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/obrienross'),
          ('github', 'http://github.com/rossobrien'),)

DEFAULT_PAGINATION = 10
