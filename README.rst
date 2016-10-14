LCRS website
------------

Made with Django and Wagtail.

Running locally::

    mkvirtualenv lcrsweb
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
