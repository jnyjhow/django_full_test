#!/bin/bash

cd src/
python manage.py makemigrations
python manage.py migrate
python manage.py test
