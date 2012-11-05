#!~/envs/{{ project_name }}/bin/python

import sys, os
import site


PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
DJANGOPROJECT = '{{ project_name }}'

print "DJANGOPROJECT: ", DJANGOPROJECT

# Add PROJECT_DIR to site
site.addsitedir(PROJECT_DIR)

# Point to settings module
os.environ['DJANGO_SETTINGS_MODULE'] = "%s.settings" % DJANGOPROJECT

# Switch to the directory of your project. (Optional.)
os.chdir(PROJECT_DIR)

print >> sys.stderr, sys.path
sys.stderr.flush()

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
