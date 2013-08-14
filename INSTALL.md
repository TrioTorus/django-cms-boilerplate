Get the source and install dependencies
=======================================
Before you begin: you need to have git, Fabric and virtualenvwrapper
installed on your computer. Then do the following:

    $ git clone git@bitbucket.org:dries/{{ project_name}}.git
    $ cd {{ project_name}}
    $ fab localhost bootstrap
    $ workon {{ project_name}}
    $ git init
    $ fab localhost db_create


Create the tables
=================
Edit settings.py, enter your database details. Then:

    $ ./manage.py syncdb --all
    $ ./manage.py migrate --fake


Running the project
===================
You can run the development server with Django's runserver:

    $ ./manage.py runserver
