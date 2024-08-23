#!/bin/bash

# Navega para o diretório do projeto
cd src/

# Executa as migrações e testes
python manage.py makemigrations
python manage.py migrate
python manage.py test
