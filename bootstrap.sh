# Initializes development environment.
# Source this script, don't run it.
# Requires virtualenvwrapper!

mkvirtualenv {{ project_name }}
pip install -r requirements_dev.txt
setvirtualenvproject
echo 'export DJANGO_SETTINGS_MODULE={{ project_name }}.settings.dev'>$WORKON_HOME/{{ project_name }}/bin/postactivate 
chmod +x ./manage.py