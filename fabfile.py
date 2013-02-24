from __future__ import with_statement
import os
from fabric.api import *
from fabric.contrib import django
import site

env.projectname = "{{ project_name }}"
django.project('%(projectname)s' % env)
from django.conf import settings
env.repo = "git@bitbucket.org:dries/%(projectname)s" % env
env.less = False
django.settings_module('%(projectname)s.settings.dev' % env )

def production():
    """ Use production server settings """
    
    env['suffix'] = "prod"
    env['hosts']=['urga@ssh.alwaysdata.com:22']
    env['projectdir'] = "$HOME/src/%(projectname)s-%(suffix)s" % env
    env['mediadir'] = "~/www/media-%(projectname)s-%(suffix)s" % env
    env['branch'] = 'master'
    env['venv'] = "%(projectname)s-%(suffix)s" % env
    env['settings_module'] = "%(projectname)s.settings.%(suffix)s" % env
    django.settings_module(env['settings_module'])
    
def staging():
    """ Use staging server settings """
    
    env['suffix'] = "staging"
    env['hosts']=['urga@ssh.alwaysdata.com:22']
    env['projectdir'] = "$HOME/src/%(projectname)s-%(suffix)s" % env
    env['mediadir'] = "~/www/media-%(projectname)s-%(suffix)s" % env
    env['branch'] = 'develop'
    env['venv'] = "%(projectname)s-%(suffix)s" % env
    env['settings_module'] = "%(projectname)s.settings.%(suffix)s" % env
    django.settings_module(env['settings_module'])

def init_virtualenv():
    run("mkvirtualenv %(venv)s" % env)
    with cd('$WORKON_HOME/%(venv)s' % env):
        run('echo "%(projectdir)s" > .project' % env) # single quotes are important here.
        
    with prefix('workon %(venv)s' % env):
        run("pip install -r requirements.txt")

def update(skipreq=True):
    "Update the deployment. By default it skips checking requirements. Use skipreq=True to force updating requirements."
    with prefix('workon %(venv)s' % env):
        run('git pull')
        if env.less:
            run('lessc -x %(projectname)s/static/less/style.less > %(projectname)s/static/css/style.css' % env)
        if not skipreq:
            run('pip install -r requirements.txt --upgrade')
        run('./manage.py collectstatic --noinput --settings=%(settings_module)s' % env)
        run('cp apache/.htaccess public/')
        run('cp apache/django_%(suffix)s.fcgi public/django.fcgi' % env)

def deploy():
    """Delete and initialize deployment on the target server"""
    run("rm -rf %(projectdir)s" % env)
    run("git clone -b %(branch)s %(repo)s %(projectdir)s" % env )
    init_virtualenv()
    update(skipreq=False)

def dumpdata():
    site.addsitedir(os.path.abspath(os.path.dirname(__file__)))
    from django.conf import settings
    local("PGPASSWORD=%s pg_dump -O -x -h %s -U %s %s > dumpdata.sql" % (
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

def getmedia():
    local('rm -r public/media')
    local('mkdir public/media')
    get('%(mediadir)s/*' % env, 'public/media/')

def putmedia():
    run('mkdir -p %(mediadir)s' % env)
    run('ln -snf %(mediadir)s %(projectdir)s/public/media' % env)
    put('public/media/*', '%(mediadir)s' % env)