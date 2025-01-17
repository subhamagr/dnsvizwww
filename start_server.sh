#!/usr/bin/env bash

python3 /deploy/app/manage.py migrate --run-syncdb

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    python3 /deploy/app/manage.py createsuperuser --no-input
fi

python3 /deploy/app/manage.py runserver 0.0.0.0:8000
