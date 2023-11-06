#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jonathan Mair'
SITENAME = u'Jonathan Mair'
SITESUBTITLE = u'Out of the frying pan.'
SITEURL = 'https://www.jonathanmair.com'

PATH = 'content'

DEFAULT_DATE = 'fs'

DEFAULT_DATE_FORMAT = '%-d/%-m/%Y'
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'jp': '%Y-%m-%d(%a)',
}
LOCALE = 'en_GB'


TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ATOM = None
FEED_RSS = None
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll

LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)


# Social widget
SOCIAL = (#('Facebook', 'http://facebook.com/arulraj.net'),
          ('Twitter', 'http://twitter.com/urtnas'),
          ('Github', 'https://github.com/JonathanMair')
          )

# Pagination
DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['assets']
EXTRA_PATH_METADATA = {
    'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
    'assets/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'assets/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'assets/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'assets/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'assets/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'assets/CNAME': {'path': 'CNAME'}
}

# Post and Pages path
ARTICLE_URL = '{date:%Y}-{date:%m}-{date:%d}-{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}-{date:%m}-{date:%d}-{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
YEAR_ARCHIVE_URL = ''
YEAR_ARCHIVE_SAVE_AS = ''
MONTH_ARCHIVE_URL = ''
MONTH_ARCHIVE_SAVE_AS = ''

# Tags and Category path
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'
CATEGORIES_URL = ''
CATEGORIES_SAVE_AS = ''
TAG_URL = ''
TAG_SAVE_AS = ''
TAGS_URL = 'tag/'
TAGS_SAVE_AS = 'tag/index.html'

# Author
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_URL = ''
AUTHORS_SAVE_AS = ''

#Archives
ARCHIVES_URL = 'archive/'
ARCHIVES_SAVE_AS = 'archive/index.html'

# To show the line numbers for code blocks
# Refer https://docs.getpelican.com/en/stable/settings.html?highlight=MARKDOWN#basic-settings
# MARKDOWN = {
#   'extension_configs': {
#     'markdown.extensions.codehilite': {'css_class': 'highlight', 'linenums': True},
#     'markdown.extensions.extra': {},
#     'markdown.extensions.meta': {},
#   },
#   'output_format': 'html5',
# }
# PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

### Plugins

PLUGIN_PATHS = [
  'pelican-plugins'
]

PLUGINS = [
  'sitemap',
  'neighbors',
  'assets',
  'post_stats',
]

IGNORE_FILES = [
'includes'
]

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Analytics
# GOOGLE_ANALYTICS = "UA-3546274-12"

THEME = '/Users/jonathanmair/pelican-themes/attila-1.6'

### Theme specific settings

# To set background image for the home page.
HOME_COVER = 'assets/images/banner.jpg'
# JM: added this...
HEADER_COVER = 'assets/images/banner.jpg'

# Custom Header

TAG_META = {
  "cupcake": {
    "cover": "assets/images/rainbow_cupcake_cover.png",
    "description": "Cupcake ipsum dolor sit amet. Topping",
  },
  "general": {
    "cover": "https://images.unsplash.com/photo-1486427944299-d1955d23e34d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80",
    "description": "General ipsum dolor sit amet. Topping"
  },
  "getting started": {
    "color": "MediumSeaGreen",
    "description": "Getting Started ipsum dolor sit amet. Topping"
  }
}

CATEGORY_META = {
  "examples": {
    "cover": "https://images.unsplash.com/photo-1645113720391-279a153b4f53?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2073&q=80",
    "description": "Examples ipsum dolor sit amet. Topping"
  },
  "misc": {
    "color": "SlateBlue",
    "description": "Misc ipsum dolor sit amet. Topping"
  }
}




# JM: This needs to be AUTHOR*S*_BIO: was missing the 'S'
AUTHORS_BIO = {
  "jonathan mair": {
    "name": "Jonathan Mair",
    "cover": "assets/images/banner.jpg",
    "image": "assets/images/jonathan-mair.jpg",
    # "website": "https://www.jonathanmair.com",
    "linkedin": "jonathan-mair-phd",
    "github": "JonathanMair",
    "twitter": "urtnas",
    "location": "Sevilla",
    "bio": '''Anthropologist, ethnographer, qualitative research designer,
            social scientist, coder and data ethnusiast. 
          '''
  }
}

MENUITEMS = (('Home', '/'),
             ('About', '/about/'),
             ('Anthropology', '/anthropology/'),
             ('Archives','/archive/'),
             ('Tags', '/tag/'),
             ('Publications', '/publications/'))

SHOW_ARTICLE_MODIFIED_TIME = True
SHOW_AUTHOR_BIO_IN_ARTICLE = True
SHOW_CATEGORIES_ON_MENU = False
SHOW_COMMENTS_COUNT_IN_ARTICLE_SUMMARY = False
SHOW_CREDITS = False
SHOW_FULL_ARTICLE_IN_SUMMARY = True
SHOW_PAGES_ON_MENU = False
SHOW_SITESUBTITLE_IN_HTML_TITLE = False
SHOW_TAGS_IN_ARTICLE_SUMMARY = True


COLOR_SCHEME_CSS = 'tomorrow.css'
CSS_OVERRIDE = ['assets/css/myblog.css']

# Jinja config - Pelican 4
JINJA_ENVIRONMENT = {
  'extensions' :[
    'jinja2.ext.loopcontrols',
    'jinja2.ext.i18n',
    'jinja2.ext.do',
  ]
}

# JINJA_FILTERS = {'max': max}

PANDOC_EXTENSIONS = [
    "smart",
    # "+footnotes",   # Enabled extension
    # "-pipe_tables", # Disabled extension
]

PANDOC_DEFAULTS_FILES = [
    "pandocdefaults.yaml",
]

TYPOGRIFY = True

WITH_FUTURE_DATES = True

# Comments
DISQUS_SITENAME = "jonathanmair"

THEME_TEMPLATES_OVERRIDES = ["includes/"]

PAGE_ORDER_BY = 'page_order'