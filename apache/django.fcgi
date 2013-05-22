#!/bin/bash

export DJANGO_SETTINGS_MODULE=attitude.settings.dev
source $WORKON_HOME/attitude/bin/activate
typeset project_dir=$(cat "$VIRTUAL_ENV/$VIRTUALENVWRAPPER_PROJECT_FILENAME");
cd "$project_dir";
python -c 'from django.core.servers.fastcgi import runfastcgi;runfastcgi(method="threaded", daemonize="false")'
