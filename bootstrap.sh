# Initializes development environment.
# Source this script, don't run it.
# Requires virtualenvwrapper!

mkvirtualenv {{ project_name }}
pip install -r requirements_dev.txt
setvirtualenvproject
