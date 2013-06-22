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

    django-admin.py startproject --template https://github.com/driesdesmet/django-cms-boilerplate/archive/master.zip --extension py,md,gitignore,dist,fcgi,html YOURPROJECTNAME



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

Check instructions in INSTALL.md

Open browser to [http://127.0.0.1:8000](http://127.0.0.1:8000) -- if all went well you should see the "It works!" page.
