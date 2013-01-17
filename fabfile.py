from __future__ import with_statement
import os
from fabric.api import *
from fabric.contrib import django
import site
from django.conf import settings

env.projectname = "{{ project_name }}"
env.repo = "git@bitbucket.org:dries/%(projectname)s" % env
django.project(env.projectname)

def production():
    """ Use production server settings """
    
    env.hosts=['urga@ssh.alwaysdata.com:22']
    env['projectdir'] = "$HOME/src/%(projectname)s-prod" % env
    env['branch'] = 'master'
    env['venv'] = "%(projectname)s-prod" % env
    django.settings_module("%(projectname)s.settings_dev" % env)
    
def stage():
    """ Use staging server settings """
    
    env.hosts=['urga@ssh.alwaysdata.com:22']
    env['projectdir'] = "$HOME/src/%(projectname)s-stage" % env
    env['branch'] = 'develop'
    env['venv'] = "%(projectname)s-stage" % env
    django.settings_module("%(projectname)s.settings_stage" % env)

def init_virtualenv():
    run("mkvirtualenv %(venv)s" % env)
    with cd('$WORKON_HOME/%(venv)s' % env):
        run('echo "%(projectdir)s" > .project' % env) # single quotes are important here.
        
    with prefix('workon %(venv)s' % env):
        run("pip install -r requirements.txt")

def update():
    with prefix('workon %s' % env.venv):
        run('git pull')
        run('lessc -x %(projectname)s/static/less/style.less > %(projectname)s/static/css/style.css' % env)
        run('./manage.py collectstatic --noinput')

def deploy():
    """Delete and initialize deployment on the target server"""
    run("rm -rf %(projectdir)s" % env)
    run("git clone -b %(branch)s %(repo)s %(projectdir)s" % env )
    init_virtualenv()
    update()

def copyfixturesmedia():
    local("cp -r %(projectname)s/fixtures/media/* public/media/" % env )

def savemediatofixtures():
    """Copy current user content to fixtures."""
    local("cp -r %s %(projectname)s/fixtures/" % (settings.MEDIA_ROOT, env))

def dumpdata():
    site.addsitedir(os.path.abspath(os.path.dirname(__file__)))
    from django.conf import settings
    local("PGPASSWORD=%s pg_dump -O -h %s -U %s %s > dumpdata.sql" % (
        settings.DATABASES['default']['PASSWORD'],
        settings.DATABASES['default']['HOST'],
        settings.DATABASES['default']['USER'],
        settings.DATABASES['default']['NAME'],
        )
    )

def restoredata():
    site.addsitedir(os.path.abspath(os.path.dirname(__file__)))
    from django.conf import settings
    local("PGPASSWORD=%s psql -1 -h %s -U %s %s < dumpdata.sql" % (
        settings.DATABASES['default']['PASSWORD'],
        settings.DATABASES['default']['HOST'],
        settings.DATABASES['default']['USER'],
        settings.DATABASES['default']['NAME'],
        )
    )
