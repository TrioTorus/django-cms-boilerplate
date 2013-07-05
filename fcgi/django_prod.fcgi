#!/bin/bash

source /home/urga/.bash_profile
workon {{ project_name }}
python -c 'from django.core.servers.fastcgi import runfastcgi;runfastcgi(method="threaded", daemonize="false")'
