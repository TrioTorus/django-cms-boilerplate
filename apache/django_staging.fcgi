#!/bin/bash

export DJANGO_SETTINGS_MODULE={{ project_name }}.settings.staging
source $WORKON_HOME/{{ project_name }}-staging/bin/activate
typeset project_dir=$(cat "$VIRTUAL_ENV/$VIRTUALENVWRAPPER_PROJECT_FILENAME");
cd "$project_dir";
python -c 'from django.core.servers.fastcgi import runfastcgi;runfastcgi(method="threaded", daemonize="false")'
