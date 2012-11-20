from __future__ import with_statement
import os
from fabric.api import *
from fabric.contrib import django

django.project('{{ project_name }}')
from django.conf import settings

env.projectname = "{{ project_name }}"
env.repo = "git@bitbucket.org:dries/%(projectname)s" % env

def production():
    """ Use production server settings """
    
    env.hosts=['urga@ssh.alwaysdata.com:22']
    env['projectdir'] = "~/src/%(projectname)s-prod" % env
    env['branch'] = 'master'
    env['venv'] = env.projectname
    
def staging():
    """ Use staging server settings """
    
    env.hosts=['urga@ssh.alwaysdata.com:22']
    env['projectdir'] = "~/src/%(projectname)s-stage" % env
    env['branch'] = 'develop'
    env['venv'] = "%(projectname)s-stage" % env

def bootstrap():
    run("mkvirtualenv {{ project_name }}")
    run("pip install -E {{ project_name }} -r requirements.txt")

def compileless():
    """Compile less locally to be saved in the repo"""
    local("lessc -x %(projectname)s/static/less/style.less > %(projectname)s/static/css/style.css" % env)

def copyfixturesmedia():
    local("cp -r %(projectname)s/fixtures/media/* public/media/" % env

def savemediatofixtures():
    """Copy current user content to fixtures."""
    local("cp -r %s %(projectname)s/fixtures/" % (settings.MEDIA_ROOT, env)

def deploy():
    """Delete and initialize deployment on the target server"""
    run("git clone -b %(branch)s %(repo)s %(projectdir)s" % env )

def update():
    compileless()
    local('git commit -a')
    local('git push')
    with cd(env['projectdir']):
        run('git pull')
    with prefix('workon %s' % env.venv):
        run('./manage.py collectstatic --noinput')