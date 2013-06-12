# Django settings for vectis project.
from os.path import normpath, dirname, abspath, join
import os
import dj_database_url

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(dirname(dirname(abspath(__file__))))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Dries Desmet', 'dries@urga.be'),
)

MANAGERS = ADMINS

DATABASES = {'default': dj_database_url.config()}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Brussels'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'nl'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
########## END GENERAL CONFIGURATION

LANGUAGES = (
    ('nl', 'Nederlands'),
)

########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
########## END STATIC FILE CONFIGURATION

########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
########## END SECRET CONFIGURATION

########## SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []
########## END SITE CONFIGURATION

########## FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)
########## END FIXTURE CONFIGURATION

########## TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',

    # Django CMS
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)


# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
)
########## END TEMPLATE CONFIGURATION

ROOT_URLCONF = '{{ project_name }}.urls'

MIDDLEWARE_CLASSES = (
    
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    #Django CMS
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

THIRD_PARTY_APPS = (

    # Django CMS:
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
    'cms.plugins.file',
    'cms.plugins.link',
    'cms.plugins.picture',
    'cms.plugins.text',
    'easy_thumbnails',
)

LOCAL_APPS = (
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

# EMAIL
EMAIL_HOST = "smtp.alwaysdata.com"
EMAIL_PORT =  587
EMAIL_HOST_USER = "no-reply@{{ project_name }}.be"
EMAIL_HOST_PASSWORD = "DMLH08p"

# DJANGO-CMS settings:
CMS_SEO_FIELDS = True
CMS_REDIRECTS = True
CMS_TEMPLATES = (
    ('cms/default.html', 'Standaard'),
    # ('cms/default_child.html', 'Default_Child'),
    ('cms/empty.html', 'Leeg'),
    # ('cms/home.html', 'Extra_Placeholder_Page'),
    ('cms/home.html', 'Home'),
)

CMS_PLACEHOLDER_CONF = {
    'sidebar': {
        'extra_context': {'nwords': 20},
        'name': "Sidebar",
    },

    'banner_image': {
        'plugins': ['PicturePlugin'],
        # 'extra_context': {'size': (1170, 557)},
    },

    'main-content': {
        # 'extra_context': {'size': (620, 296)},
        'name': "Hoofdinhoud",
    },

    'nieuwstekst': {
        'plugins': ['TextPlugin', 'LinkPlugin', 'FilePlugin' ],
    },

    'nieuwsafbeelding': {
        'plugins': ['PicturePlugin'],
        'limits': {
            'global': 1,
        }
    }
    
}

# Tinymce

TINYMCE_DEFAULT_CONFIG = {
    'theme': "simple",
    'skin' : "urga",
    "theme_advanced_resizing" : "true",
    'height': "300px",
    # "content_css" : STATIC_URL + "css/bootstrap.css",
    "content_css" : STATIC_URL + "css/style.css",
    "plugins" : "paste",
    "paste_text_sticky": "true",
    "paste_text_sticky_default": "true",
    "theme_advanced_blockformats" : "p,h1,h2,h3,h4,h5,h6,address,code,blockquote",
    "theme_advanced_buttons1" : 
        "bold,italic,underline,strikethrough,removeformat,separator,bullist,numlist,outdent,indent,separator,undo,redo,separator,hr,charmap,visualaid,separator,formatselect,removeformat,code,help",
    # "paste_auto_cleanup_on_paste" : "true",
}