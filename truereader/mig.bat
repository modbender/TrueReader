@echo off
echo ===========MAKEMIGRATIONS========
python manage.py makemigrations
echo ===========MIGRATE============
python manage.py migrate
