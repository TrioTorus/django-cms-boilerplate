from __future__ import with_statement
import os
from os.path import abspath, basename, dirname
from fabric.api import env, local, run, require
from fabric.contrib import django
import site
from django.utils.crypto import get_random_string

# GLOBALS
#########

env['projectname'] = basename(dirname(abspath(__file__)))
env["repo"] = "git@bitbucket.org:dries/%(projectname)s" % env
env["less"] = True
env["db_engine"] = "postgres" # Use 'postgres', 'mysql' or 'sqlite'
env["remote_username"] = "urga"


# ENVIRONMENTS
##############

def localhost():
    """ Use development server settings """

    env['suffix'] = "dev"
    env['projectdir'] = dirname(abspath( __file__ ))
    env.['run'] = local
    env['requirementsfile'] = "requirements_%(suffix)s.txt" % env
    env['db_user'] = "%(projectname)s" % env
    env["db_host"] = "localhost"
    env['db_name'] = env.db_user
    django.settings_module('%(projectname)s.settings.%(suffix)s' % env )

def staging():
    """ Use staging server settings """
    
    env['suffix'] = "staging"
    env['run'] = run
    env['hosts']=['%(remote_username)s@ssh.alwaysdata.com:22' % env, ]
    env['basedir']= os.path.join(os.environ['HOME'], "www-%(suffix)" % env)
    env['projectdir'] = os.path.join(env.basedir, env.projectname)
    env['mediadir'] = os.path.join(env.basedir, env.projectname+"-media")
    env['branch'] = 'develop'
    env['venv'] = "%(projectname)s-%(suffix)s" % env
    env['requirementsfile'] = "requirements.txt"
    env['db_user'] = "%(remote_username)s_%(projectname)s" % env
    env["db_host"] = "adpostgresql.urga.be"
    env['db_name'] = "%(remote_username)s_%(projectname)s-%(suffix)s" % env
    django.settings_module("%(projectname)s.settings.%(suffix)s" % env)

def production():
    """ Use production server settings """
    
    env['suffix'] = "prod"
    env['hosts']=['%(remote_username)s@ssh.alwaysdata.com:22' % env, ]
    env['basedir']= os.path.join(os.environ['HOME'], "www")
    env['projectdir'] = os.path.join(env.basedir, env.projectname)
    env['mediadir'] = os.path.join(env.basedir, env.projectname+"-media")
    env['branch'] = 'master'
    env['venv'] = "%(projectname)s" % env
    env['requirementsfile'] = "requirements.txt"
    env['db_user'] = "%(remote_username)s_%(projectname)s" % env
    env["db_host"] = "adpostgresql.urga.be"
    env['db_name'] = "%(remote_username)s_%(projectname)s-%(suffix)s" % env
    django.settings_module("%(projectname)s.settings.%(suffix)s" % env)

# HELPERS
#########
def _generate_key():
    
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return get_random_string(50, chars)


def _generate_db_url():
    
    print "Setting up Database for %s" % env.suffix
    print "Engine: %s" % env.db_engine
    print "User: %s" % env.db_user
    print "Hostname: %s" % env.db_hostname
    print "Database name: %s" % env.db_name

    password = raw_input('DB Password: [Default: %s] ' % env.projectname)
    db_password = password or env.projectname
    
    return "%s://%s:%s@%s/%s" % (env.db_engine, db_user, db_password, db_hostname, db_name)

# COMMANDS
##########

def bootstrap():
    require("venv", provided_by=[localhost, staging, production])
    env.run("mkvirtualenv %(venv)s" % env)
    with cd(env['projectdir']:
        env.run("setvirtualenvproject")
        env.run("pip install -r %(requirementsfile)s" % env)
        env.run("echo 'export DJANGO_SETTINGS_MODULE=%(project_name)s.settings.%(suffix)s'>>$WORKON_HOME/%(venv)s/bin/postactivate" % env)
        env.run("echo 'unset DJANGO_SETTINGS_MODULE'>>$WORKON_HOME/%(venv)s/bin/postdeactivate ")
        env.run("echo 'export DJANGO_SECRET_KEY=%s'>>$WORKON_HOME/%(venv)s/bin/postactivate" % _generate_key())
        env.run("echo 'unset DJANGO_SECRET_KEY'>>$WORKON_HOME/%(venv)s/bin/postdeactivate ")
        env.run("echo 'export DATABASE_URL=%s'>>$WORKON_HOME/%(venv)s/bin/postactivate" % _generate_db_url())
        env.run("echo 'unset DATABASE_URL'>>$WORKON_HOME/%(venv)s/bin/postdeactivate ")
        env.run("chmod +x ./manage.py")
        

def update(skipreq=True):
    "Update the remote target. By default it skips checking requirements. Use 'update:skipreq=False' to force updating requirements."

    with prefix('workon %(venv)s' % env):
        run('git pull')
        if env.less:
            run('lessc -x %(projectname)s/static/less/style.less > %(projectname)s/static/css/style.css' % env)
        if skipreq in ("False", "false"): # Have to test against a string, because the skipreq parameter is not a boolean, but a string.
            run('pip install -r requirements.txt --upgrade')
        run('./manage.py collectstatic --noinput --settings=%(settings_module)s' % env)
        run('cp apache/.htaccess public/')
        run('cp apache/django_%(suffix)s.fcgi public/django.fcgi' % env)

def deploy():
    """Delete and initialize deployment on a remote server"""

    run("rm -rf %(projectdir)s" % env)
    run("git clone -b %(branch)s %(repo)s %(projectdir)s" % env )
    bootstrap()
    update(skipreq=False)

def dumpdata():
    "Dump sql to local file named dumpdata.sql using pg_dump."

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