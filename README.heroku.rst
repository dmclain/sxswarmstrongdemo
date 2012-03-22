Demo on Heroku
==============

This project is set up to run on Heroku out of the box.


Getting Started
---------------

1. Sign up for Heroku, install the toolbelt, and log in as described in `Heroku's "Getting Started" guide`_.
2. Create an app on Heroku by running ``heroku create --stack cedar``.
3. Add a free shared database by running ``heroku addons:add shared-database:5mb``.
4. Set up a few environment variables:

   ::

     heroku config:add PYTHONPATH=.
     heroku config:add DJANGO_SETTINGS_MODULE=settings.heroku

5. Create the database tables by running ``heroku run django-admin.py syncdb``.
6. Prepare the database for the loaded data by running ``heroku run scripts/delete_content_types.py``.
7. Load the demo data by running ``heroku run django-admin.py loaddata demo.db.json``.
8. Push the code to Heroku by running ``git push heroku master``.
9. Start the webserver by running ``heroku ps:scale web=1``.

.. _Heroku's "Getting Started" guide: http://devcenter.heroku.com/articles/quickstart