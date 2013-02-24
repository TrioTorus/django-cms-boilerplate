from .common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ project_name }}',                      # Or path to database file if using sqlite3.
        'USER': '{{ project_name }}',                      # Not used with sqlite3.
        'PASSWORD': '{{ project_name }}',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
    # ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # ...
)

INTERNAL_IPS = ('127.0.0.1',)


INSTALLED_APPS = INSTALLED_APPS + (
    'debug_toolbar',
)

DEBUG_TOOLBAR_CONFIG = {
	'INTERCEPT_REDIRECTS': False,
}