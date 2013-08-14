from .common import *
from os.path import normpath, dirname, join, basename
import dj_database_url


DATABASES['default'] =  dj_database_url.config()

ALLOWED_HOSTS = ['www.{{ project_name }}.be']

########## STATIC FILE CONFIGURATION
STATIC_ROOT = normpath(join(dirname(SITE_ROOT), basename(SITE_ROOT) + "-static"))
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = 'http://static.{{ project_name }}.be/'
########## END STATIC FILE CONFIGURATION

########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(dirname(SITE_ROOT), basename(SITE_ROOT)+"-static", "media"))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = STATIC_URL + 'media/'
########## END MEDIA CONFIGURATION
