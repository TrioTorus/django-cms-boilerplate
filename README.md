{% if False %}
# Django 1.4 with HTML5★Boilerplate Project Template

## About

This is a starting template for Django 1.4 projects using (a slightly modified version of) [HTML5 Boilerplate](http://html5boilerplate.com).

## Features ##

* Global assets, web, templates and fixtures directory.
* Collects static and media into public/{static,media} respectively.
* Django admin activated by default.
* Django timezone setting changed to UTC for sanity.
* HTML 5 base template with simple 404 and 500 error templates.
* Discourages storing credentials and secrets in the repository.
* Encourages the use of developer/machine specific `settings.py` file.
* Encourages the use of virtualenv and virtualenvwrapper.
* Encourages the use of pip and `requirements.txt`.
* Encourages the use of git.
* Includes a .gitignore for the usual junk.
* Automatically builds a README with installation notes.

## How to use this template to create your project ##

* Install Django 1.4
* Run the following one of the following commands, specifying your project name:
        
    * To use plain CSS:

            django-admin.py startproject --template https://github.com/TrioTorus/django-project-skel/zipball/master --extension py,md,gitignore,dist yourprojectname

    * To use LESS:

            django-admin.py startproject --template https://github.com/TrioTorus/django-project-skel/zipball/less --extension py,md,gitignore,dist yourprojectname
    
    * To use Twitter's Bootstrap
    
            django-admin.py startproject --template https://github.com/TrioTorus/django-project-skel/zipball/bootstrap --extension py,md,gitignore,dist yourprojectname


{% endif %}
# {{ project_name|title }} Django Project #

## About ##

Describe {{ project_name }} here.

## Prerequisites ##

* Python >= 2.5
* pip
* virtualenv (virtualenvwrapper is recommended for use during development)

## Installation ##

### Creating the environment ###

Create a virtual python environment for the project.
If you're not using virtualenv or virtualenvwrapper you may skip this step.

#### For virtualenvwrapper ####

        mkvirtualenv --no-site-packages {{ project_name }}-env

#### For virtualenv ####

        virtualenv --no-site-packages {{ project_name }}-env
        source {{ project_name }}-env/bin/activate

### Clone the code ###

Obtain the url to your git repository.

        git clone <URL_TO_GIT_RESPOSITORY> {{ project_name }}

### Install requirements ###

        cd {{ project_name }}
        pip install -r requirements.txt

### Configure project ###
When you're finished installing requirements, you'll need to set up your local settings.py file:

        cp {{ project_name }}/settings.py.dist {{ project_name }}/settings.py
        vim {{ project_name }}/settings.py

### Sync database ###
After you configure your local settings (database, etc.) you're ready to run `syncdb`:

        python manage.py syncdb

## Running ##
Once that's completed you can boot up the dev server:

        python manage.py runserver

Open browser to [http://127.0.0.1:8000](http://127.0.0.1:8000) -- if all went well you should see the "It works!" page.
