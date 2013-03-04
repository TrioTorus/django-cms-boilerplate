# Global settings for {{ project_name }} project.
from os.path import abspath, dirname, join

REPO_ROOT = dirname(dirname(dirname(abspath( __file__ ))))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Dries Desmet', 'dries@urga.be'),
)

MANAGERS = ADMINS

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

LANGUAGES = [
##    ('en', 'English'),
    ('nl', 'Nederlands'),
    # ('fr', 'Frans'),
]

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = join(REPO_ROOT, 'public', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ secret_key }}'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = join(REPO_ROOT, 'public', 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    # 'simple_translation.middleware.MultilingualGenericsMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    
)

#EMAIL
EMAIL_HOST = "smtp.alwaysdata.com"
EMAIL_PORT =  587
EMAIL_HOST_USER = "no-reply@{{ project_name }}.be"
EMAIL_HOST_PASSWORD = "DMLH08p"


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',

    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

INSTALLED_APPS = (
    '{{ project_name }}',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    
    # 'ajax',

    # Django-cms:
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
    'cms.plugins.file',
    'cms.plugins.link',
    'cms.plugins.picture',
    'cms.plugins.text',
    # 'cmsplugin_blog',
    # 'cmsplugin_gallery',
    # 'inline_ordering',
    'cmsworkaround',
    'easy_thumbnails',
    'tinymce',
    # 'tagging', # Dependancy of cmsplugin_blog
    # 'simple_translation', # Dependancy of cmsplugin_blog
    # 'djangocms_utils', # Dependancy of cmsplugin_blog

    'form_designer',
    'form_designer.contrib.cms_plugins.form_designer_form',
)

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

# CMSPLUGIN_BLOG settings:
JQUERY_UI_CSS = 'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/themes/smoothness/jquery-ui.css'
JQUERY_UI_JS = 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/jquery-ui.min.js'
JQUERY_JS = 'https://ajax.googleapis.com/ajax/libs/jquery/1.8.0/jquery.min.js'
CMSPLUGIN_BLOG_PLACEHOLDERS = ('nieuwstekst', 'nieuwsafbeelding')


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