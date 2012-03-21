#!/bin/sh
django-admin.py loaddata demo.db.json
django-admin.py runserver 0.0.0.0:$PORT
