#!/bin/bash

sudo apt install python3
pip install django-admin
pip install django
sudo apt install sqlite3
cd nitkjuma
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver 8082
