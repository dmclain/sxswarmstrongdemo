#!/bin/sh
export PYTHONPATH=.
export DJANGO_SETTINGS_MODULE=settings.heroku
django-admin.py loaddata demo.db.json
django-admin.py runserver 0.0.0.0:$PORT
