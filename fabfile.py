from __future__ import with_statement
import os
from fabric.api import *

REPO = "git@bitbucket.org:dries/{{ project_name }}"

def bootstrap():
    run("mkvirtualenv {{ project_name }}")
    run("pip install -E {{ project_name }} -r requirements.txt")

def production():
    """ Use production server settings """
    
    env.hosts=['urga@ssh.alwaysdata.com:22']
    env['projectdir'] = "~/src/{{ project_name }}"
    env['branch'] = 'master'
    
def staging():
    """ Use staging server settings """
    
    env.hosts=['urga@ssh.alwaysdata.com:22']
    env['projectdir'] = "~/src/{{ project_name }}-stage"
    env['branch'] = 'develop'

def deploy():
    """Delete and initialize deployment on the target server"""
    #run("rm -rf %s" % env['projectdir'])
    run("git clone -b %s %s %s" % (env.branch, REPO, env.projectdir) )

def update():
    with cd(env['projectdir']):
        run('git pull')
