#!/bin/bash

python manage.py test
python manage.py makemigrations
python manage.py migrate

