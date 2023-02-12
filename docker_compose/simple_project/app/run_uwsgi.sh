#!/usr/bin/env bash

set -e

chown www-data:www-data /var/log

python manage.py makemigrations
uwsgi --strict --ini ./app/uwsgi.ini
