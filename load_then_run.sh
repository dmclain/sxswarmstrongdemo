#!/bin/sh
export PYTHONPATH=.
armstrong loaddata demo.db.json
django-admin.py runserver 0.0.0.0:$PORT --settings=settings.heroku
