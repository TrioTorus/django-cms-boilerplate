#!/home/urga/envs/{{ project_name }}-prod/bin/python

from os.path import dirname,abspath,basename
import logging
import sys, os
import site

PROJECT_DIR = dirname(dirname(abspath( __file__ )))
BASENAME = basename(PROJECT_DIR)
DJANGOPROJECT = '{{ project_name }}'

logger = logging.getLogger(__name__)

# Add PROJECT_DIR to site
site.addsitedir(PROJECT_DIR)

# Point to settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.prod")

# Switch to the directory of your project. (Optional.)
os.chdir(PROJECT_DIR)

logger.info("Starting project: %s" % BASENAME)


from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
