# Download virtualenv
pip3 install virtualenv

# Create virtualenv having python 3.6
virtualenv -p python3 projectenv

# Activate virtual env
source bin/activate
source ./script/activate # For Windows
deactivate 

# Make source code 
mkdir src

# Install django
pip install django

# View dependencies
pip freeze

Navigate to src folder
ls -a # Show hidden folder

# Write all the dependencies in requirement.txt file
pip freeze > requirement.txt

# Read file
cat requirement.txt

# Git stages => Working Directory > Staging > Commit > Push (Remote)
# At commit, then worked is saved to local repo

# View git log
git log

# To view list of commands for django-admin
django-admin

# Create project with manage.py file
django-admin startproject projectname .

# Remove project
rm -rf projectname

# Create git ignore file so that unneeded files don't get pushed in Remote repo
touch .gitignore 

# Open folder in subl
subl .

'''
	Copy code from https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore and paste in .gitignore
	Also copy code from https://gist.github.com/santoshpurbey/6f982faf1eacdac153ffd86a3a694239 and paste in .gitignore
	under django stuff 
'''

# View subcommands for manage.py
python manage.py

# Create/Update db.sqlite3 (Database), generates schema/code ready to be migrated for the database
# ORM => Object Relational Mapping
python manage.py makemigrations

# Python Support postgreSQL

# To migrate database
python manage.py migrate

# Run server
python manage.py runserver

# Create a superuser
'''
	Username: sunil
	pwd: abc54321
'''
python manage.py createsuperuser
