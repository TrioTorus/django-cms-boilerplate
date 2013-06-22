from __future__ import with_statement
import os
from os.path import abspath, basename, dirname, join
from fabric.api import env, local, run, require, prompt, cd, prefix, execute, settings
from fabric.colors import yellow as _yellow
from fabric.contrib import django
import site
from django.utils.crypto import get_random_string
import inspect
from datetime import datetime
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse


# GLOBALS
#########

env['projectname'] = basename(dirname(abspath(__file__)))
env["repo"] = "git@bitbucket.org:dries/%(projectname)s" % env
env["less"] = True
env["db_engine"] = "postgres" # Use 'postgres', 'mysql' or 'sqlite'


def _set_alwaysdata_env():
    env['run'] = run
    env['accountname'] = "urga"
    env['hosts']=['%(accountname)s@ssh.alwaysdata.com' % env, ]
    env['venv'] = "%(projectname)s" % env
    env['requirementsfile'] = "requirements.txt"

    env['homedir']=join("/home", "%(accountname)s" % env )
    env['basedir']= join(env.homedir, "www")
    env['projectdir'] = join(env.basedir, env.projectname)
    env['staticdir'] = join(env.basedir, env.projectname+"-static")

    env['db_user'] = "%(accountname)s_%(projectname)s" % env
    env["db_host"] = "adpostgresql.urga.be"
    env['db_name'] = "%(accountname)s_%(projectname)s" % env

# ENVIRONMENTS
##############

def localhost():
    """
    Use development server settings
    """
    env['settings'] = "dev"
    env['run'] = local
    env['venv'] = "%(projectname)s" % env
    env['requirementsfile'] = "requirements_%(settings)s.txt" % env
    
    env['projectdir'] = dirname(abspath( __file__ ))
    
    env['db_user'] = "%(projectname)s" % env
    env["db_host"] = "localhost"
    env['db_name'] = env.db_user
    

def staging():
    """
    Use staging server settings
    """
    env['settings'] = "staging"
    env['projectname'] = "%(projectname)s-%(settings)s" % env
    env['branch'] = 'develop'
    _set_alwaysdata_env()

def production():
    """
    Use production server settings
    """
    env['settings'] = "prod"
    env['branch'] = 'master'
    _set_alwaysdata_env()

# HELPERS
#########
def _generate_key():
    """
    Generate a random key just like django-startproject does it.
    """
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*-_=+()'
    return get_random_string(50, chars)


def _generate_db_url():
    
    print "Setting up Database for %s" % env.settings
    print "Engine: %s" % env.db_engine
    print "User: %s" % env.db_user
    print "Hostname: %s" % env.db_host
    print "Database name: %s" % env.db_name

    if not env.settings=="dev":
        db_password = prompt(_yellow('DB Password: '))
    else:
        db_password = env.projectname

    return "%s://%s:%s@%s/%s" % (env.db_engine, env.db_user, db_password, env.db_host, env.db_name)

def virtualenv(command):
    """
    Run command in virtualenv.
    """
    with prefix('source virtualenvwrapper.sh && workon %(venv)s' % env):
        return env.run(command)

def _fn():
    """
    Returns current function name
    """
    return inspect.stack()[1][3]

def _db_getdict():
    if not env.settings=="dev":
        db_url = virtualenv("echo $DATABASE_URL")
    else:
        db_url = os.environ['DATABASE_URL']
    parsed_url = urlparse.urlparse(db_url)

    db_dict = {
        'PASSWORD' : parsed_url.password,
        'HOST' : parsed_url.hostname,
        'USER' : parsed_url.username,
        'NAME' : parsed_url.path[1:],
    }
    return db_dict
def _db_exists():
    d = _db_getdict()
    shellreturn = local("PGPASSWORD=%(PASSWORD)s psql -l -h %(HOST)s -U %(USER)s| grep %(NAME)s | wc -l" % d, capture=True)
    return int(shellreturn)

# COMMANDS
##########

def bootstrap():
    """
    Initialize a virtual environment and configure variables
    """
    require("settings", provided_by=[localhost, staging, production])
    with cd("%(projectdir)s" % env):
        env.run("source virtualenvwrapper.sh && mkvirtualenv %(venv)s && setvirtualenvproject" % env)
    virtualenv("pip install -r %(requirementsfile)s" % env)
    virtualenv("echo 'export DJANGO_SETTINGS_MODULE=%(projectname)s.settings.%(settings)s'>>$WORKON_HOME/%(venv)s/bin/postactivate" % env)
    virtualenv("echo 'unset DJANGO_SETTINGS_MODULE'>>$WORKON_HOME/%(venv)s/bin/postdeactivate" % env)
    virtualenv("""echo "export DJANGO_SECRET_KEY='%s'">>$WORKON_HOME/%s/bin/postactivate""" % (_generate_key(), env.venv))
    virtualenv("echo 'unset DJANGO_SECRET_KEY'>>$WORKON_HOME/%(venv)s/bin/postdeactivate " % env)
    virtualenv("""echo "export DATABASE_URL='%s'">>$WORKON_HOME/%s/bin/postactivate""" % (_generate_db_url(), env.venv))
    virtualenv("echo 'unset DATABASE_URL'>>$WORKON_HOME/%(venv)s/bin/postdeactivate" % env)
    virtualenv("chmod +x ./manage.py")
        

def update_requirements():
    with prefix("source virtualenvwrapper.sh && workon %(venv)s" % env):
        env.run('pip install -r requirements.txt --upgrade')

def update(skipreq=True):
    """
    Update the remote target. By default it skips checking requirements. Use 'update:skipreq=False' to force updating requirements.
    """

    with prefix('workon %(venv)s' % env):
        env.run('git pull')
        if env.less:
            run('lessc -x %(projectname)s/static/less/theme-default/style.less > %(projectname)s/static/theme-default/css/style.css' % env)
        if skipreq in ("False", "false"): # Have to test against a string, because the skipreq parameter is not a boolean, but a string.
            execute(update_requirements)
        env.run('./manage.py collectstatic --noinput --no-default-ignore')
        env.run('cp fcgi/django_%(settings)s.fcgi fcgi/django.fcgi' % env)

def deploy():
    """
    Delete and initialize deployment on a remote server
    """
    require("settings", provided_by=[staging, production])
    env.run("rm -rf %(projectdir)s" % env)
    env.run("git clone -b %(branch)s %(repo)s %(projectdir)s" % env )
    execute(bootstrap)
    update(skipreq=False)


# Database operations
#####################

def db_dump(dumpfile="sql/dumpdata.sql"):
    print(_yellow('>>> starting %s()' % _fn()))
    require("settings", provided_by=[localhost, staging, production])
    context =  _db_getdict()
    context['DUMPFILE'] = dumpfile
    local("PGPASSWORD=%(PASSWORD)s pg_dump -O -x -h %(HOST)s -U %(USER)s %(NAME)s>%(DUMPFILE)s" % context )

def db_drop():
    print(_yellow('>>> starting %s()' % _fn()))
    local("PGPASSWORD=%(PASSWORD)s dropdb -h %(HOST)s -U %(USER)s %(NAME)s" % _db_getdict())

def db_create():
    print(_yellow('>>> starting %s()' % _fn()))
    local("PGPASSWORD=%(PASSWORD)s createdb -h %(HOST)s -O %(USER)s %(NAME)s " % _db_getdict())

def db_restore(dumpfile="sql/dumpdata.sql"):
    print(_yellow('>>> starting %s()' % _fn()))
    require("settings", provided_by=[localhost, staging, production])
    if _db_exists():
        filename = "sql/%s" % env.settings + datetime.now().strftime('_%H_%M_%d_%m_%Y.sql')
        db_dump(dumpfile=filename)
        with settings(warn_only=True):
            db_drop()
    with settings(warn_only=True):
        db_create()
    context = _db_getdict()
    context['DUMPFILE'] = dumpfile
    local("PGPASSWORD=%(PASSWORD)s psql -1 -h %(HOST)s -U %(USER)s %(NAME)s < %(DUMPFILE)s" % context )

def getmedia():
    require("settings", provided_by=["staging", "production"])
    local('rsync -r -L --delete -vv %(host_string)s:%(staticdir)s/media/ public/media' % env)

def putmedia():
    require("settings", provided_by=["staging", "production"])
    local('rsync -r -L --delete -vv public/media/ %(host_string)s:%(staticdir)s/media/' % env)