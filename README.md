{% if False %}
# Django Project Template


## About

This is a starting Django project template for [Django-CMS](http://www.django-cms.org/) projects based on [HTML5 Boilerplate](http://html5boilerplate.com) and [Bootstrap](http://twitter.github.com/bootstrap/index.html).


## Features ##

* CKEditor as textarea editor, using the djangocms-text-ckeditor plugin.
* Puts media in 'media' subfolder when developing, and can easily get/put media from deployed instances.
* Django admin activated by default.
* Django timezone setting changed to Brussels because it's my timezone.
* HTML 5 base template with simple 404 and 500 error templates, based on HTML5 boilerplate AND Bootstrap.
* Encourages the use of LESS css.
* Split settings for dev/staging/prod.
* Encourages the use of pip, virtualenvwrapper and separate developer and production requirements files.
* Fabfile for easy deployment.
* Uses Pillow as a setuptools friendly PIL drop-in replacement
* Includes a .gitignore for the usual junk.
* Includes a robots.txt template that disallows all search engines for staging deployments
* Automatically builds a README with installation notes.
* Uses bootstrap's less and does NOT use html5 Boilerplate css because both use normalize


## Requirements ##

* Django > 1.5
* Virtualenvwrapper


## Step 1: How to use this template to create your project ##

Run the following command, specifying your project name:

    django-admin.py startproject --template https://github.com/TrioTorus/django-cms-boilerplate/archive/master.zip --extension py,md,gitignore,dist,fcgi YOURPROJECTNAME



## Step 2: Initialize your development environment ##

Go into your newly created project folder and type:
    
    fab localhost bootstrap

Anything that is under this line is going to end up in your project's README:

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
