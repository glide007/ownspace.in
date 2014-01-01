#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site settings.
AUTHOR = u'glide007'
AUTHOR_EMAIL = u'glide007@ownspace.in'
SITENAME = u'OwnSpace (glide007)'
TAGLINE = 'trying to be social!'
SITEURL = 'http://192.227.233.84/'
#SITEURL = 'https://www.ownspace.in/'
DEFAULT_DATE_FORMAT = ('%d-%m-%Y')

TIMEZONE = 'Asia/Calcutta'

DEFAULT_LANG = u'en'
DEFAULT_METADATA = (
)

DELETE_OUTPUT_DIRECTORY = True

# Blogroll
LINKS = (
)

# Social widget.
SOCIAL = (
    ('Github', 'http://github.com/glide007'),
    ('Twitter', 'http://twitter.com/glide007'),
    ('RSS', '/feeds/all.atom.xml'),
)

MENUITEMS = (
)

# Content path.
PATH = 'content'
PAGE_DIR = 'pages'
ARTICLE_DIR = 'articles'
STATIC_PATHS = ['images', 'files']
EXTRA_PATH_METADATA = {
    'files/github/.nojekyll': {'path': '.nojekyll'},
    'files/github/CNAME': {'path': 'CNAME'},
    'files/github/404.html': {'path': '404.html'},
    'files/github/README.md': {'path': 'README.md'},
    'files/robots.txt': {'path': 'robots.txt'},
#    'images/favicon.ico': {'path': 'favicon.ico'},
}

# URL settings
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)
ARTICLE_URL = ('articles/{slug}/')
ARTICLE_SAVE_AS = ('articles/{slug}/index.html')
PAGE_URL = ('pages/{slug}/')
PAGE_SAVE_AS = ('pages/{slug}/index.html')
PAGE_LANG_SAVE_AS = False
TAG_URL = ('tag/{slug}/')
TAG_SAVE_AS = ('tag/{slug}/index.html')
TAGS_URL = ('tags/')
TAGS_SAVE_AS = None
CATEGORY_URL = ('category/{slug}/')
CATEGORY_SAVE_AS = ('category/{slug}/index.html')
AUTHOR_SAVE_AS = False

# Feed.
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None

# Theme.
THEME = 'theme'
# COVER_IMG_URL = '/images/cover.jpg'
COVER_BG_COLOR = '#4a3823'
TYPOGRIFY = True
DEFAULT_PAGINATION = 10

# Plugin.
PLUGIN_PATH = 'plugins'
PLUGINS = ['gzip_cache', 'assets', 'optimize_images']
PYGMENTS_RST_OPTIONS = {'cssclass': 'codehilite', 'linenos': 'table'}

# Sitemap.
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'pages': 0.9,
        'indexes': 0.8,
    },
    'changefreqs': {
        'indexes': 'daily',
        'articles': 'daily',
        'pages': 'weekly'
    }
}

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True 
