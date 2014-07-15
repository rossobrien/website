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

# Static template pages
TEMPLATE_PAGES = {'pages/about.html': 'pages/about.html',
                  'pages/work.html': 'pages/work.html',
                  'pages/contact.html': 'pages/contact.html',
                }

MENUITEMS = (
 			('Home', '/index.html'),
			('Work', '/pages/work.html'),
			('About', '/pages/about.html'),
			('Contact', '/pages/contact.html'))

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/obrien_ross'),
          ('github', 'http://github.com/rossobrien'),)

DEFAULT_PAGINATION = 10
