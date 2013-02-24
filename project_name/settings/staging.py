from .common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ project_name }}-staging',                      # Or path to database file if using sqlite3.
        'USER': '{{ project_name }}',                      # Not used with sqlite3.
        'PASSWORD': 'hilde34grivano',                  # Not used with sqlite3.
        'HOST': 'adpostgresql.urga.be',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
