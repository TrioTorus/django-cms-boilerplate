# Initializes development environment.
# Source this script, don't run it.
# Requires virtualenvwrapper!

mkvirtualenv {{ project_name }} --distribute
pip install -r requirements_dev.txt
setvirtualenvproject
echo 'export DJANGO_SETTINGS_MODULE={{ project_name }}.settings.dev'>>$WORKON_HOME/{{ project_name }}/bin/postactivate 
echo 'unset DJANGO_SETTINGS_MODULE'>>$WORKON_HOME/{{ project_name }}/bin/postdeactivate 
chmod +x ./manage.py
