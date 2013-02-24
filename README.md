{% if False %}
# Django 1.4 with HTML5★Boilerplate Project Template

## About

This is a starting Django project template for [Django-CMS](http://www.django-cms.org/) projects based on [HTML5 Boilerplate](http://html5boilerplate.com) and [Bootstrap](http://twitter.github.com/bootstrap/index.html).

## Features ##

* Ready-to-go Django-cms template project.
* Uses tinymce as textarea editor, with sanitized minimalistic look.
* Collects static and media into public/{static,media} respectively.
* Django admin activated by default.
* Django timezone setting changed to CET for sanity.
* HTML 5 base template with simple 404 and 500 error templates, based on HTML5 boilerplate AND Bootstrap.
* Encourages the use of split developer/staging/production specific `settings' module.
* Encourages the use of pip and separate developer and production requirements files.
* Includes a simple but useful fabfile.
* Uses Pillow as a setuptools friendly PIL drop-in replacement
* Includes a .gitignore for the usual junk.
* Automatically builds a README with installation notes.

## Requirements ##

* Django > 1.4
* Virtualenvwrapper

## Step 1: How to use this template to create your project ##

* Install Django 1.4
* Run the following one of the following commands, specifying your project name:
        
    * To use plain CSS:

            django-admin.py startproject --template https://github.com/TrioTorus/django-project-skel/zipball/master --extension py,md,gitignore,dist,sh,fcgi yourprojectname

    * To use LESS:

            django-admin.py startproject --template https://github.com/TrioTorus/django-project-skel/zipball/less --extension py,md,gitignore,dist,sh,fcgi yourprojectname

    * To use Twitter's Bootstrap:
    
            django-admin.py startproject --template https://github.com/TrioTorus/django-project-skel/zipball/bootstrap --extension py,md,gitignore,dist,sh,fcgi yourprojectname

    * To use django-cms:
    
            django-admin.py startproject --template https://github.com/TrioTorus/django-project-skel/zipball/django-cms --extension py,md,gitignore,dist,sh,fcgi yourprojectname

## Step 2: Initialize your development environment ##

Go into your newly created project folder and type:
    
    source bootstrap.sh

{% endif %}
# {{ project_name|title }} Django Project #

## About ##

Describe {{ project_name }} here.

## Prerequisites ##

* Python >= 2.5
* pip
* virtualenv (virtualenvwrapper is recommended for use during development)

## Installation ##

### Clone the code ###

Obtain the url to your git repository.

        git clone <URL_TO_GIT_RESPOSITORY> {{ project_name }}

### Creating the environment ###

Create a virtual python environment for the project. If you're using virtualenvwrapper,
it's simple. There is a bash script in the repo that you need to source:

        source bootstrap.sh

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
