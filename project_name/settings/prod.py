from .common import *
import dj_database_url

DATABASES['default'] =  dj_database_url.config()

ALLOWED_HOSTS = ['www.{{ project_name }}.be']