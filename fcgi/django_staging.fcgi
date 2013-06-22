#!/bin/bash

export WORKON_HOME=/home/urga/envs
source /home/urga/.local/bin/virtualenvwrapper.sh
workon {{ project_name }}-staging
python -c 'from django.core.servers.fastcgi import runfastcgi;runfastcgi(method="threaded", daemonize="false")'