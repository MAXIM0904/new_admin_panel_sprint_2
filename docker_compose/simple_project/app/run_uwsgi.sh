#!/usr/bin/env bash

set -e

chown www-data:www-data /var/log


python manage.py compilemessages -l en -l ru
python manage.py collectstatic --no-input
python manage.py createsuperuser --username=UWSGI_ADMINDJ --email=UWSGI_EMAILDJ --password=UWSGI_PASSWORDDJ --noinput || true

uwsgi --strict --ini ./app/uwsgi.ini
