============
Installation
============

Requirements
============
- Python 2.7+ (no Python 3 support yet!)
- `Django 1.8 <https://www.djangoproject.com/>`_ (Django 1.9+ not supported yet!)
- `Hackstack 2.4 <http://haystacksearch.org/>`_ (Search module for Django)
- `Whoosh 2.5 <https://pypi.python.org/pypi/Whoosh/>`_ (Full-text search enginge used for django-haystack)
- `Pillow <https://pypi.python.org/pypi/Pillow/2.9.0>`_

Manual Installation
===================
- Clone source repository from `GitHub <https://github.com/holgerd77/django-website-showroom>`_
- Create a virtual environment with ``virtualenv``
- Install the requirements with ``pip install -r requirements.txt``
- Manually link the ``website_showroom`` folder to the ``site-packages`` folder of your environment

Setup
=====
Create a separate ``Django`` project::

    django-admin(.py) startproject my_showroom_project

Add ``haystack`` and the ``website_showroom`` app to ``INSTALLED_APPS`` in ``settings.py``::

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'haystack',
        'website_showroom',
    )

The following settings are necessary for ``Haystack`` (search) to work::

    # Haystack settings
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
            'PATH': os.path.join(BASE_DIR, 'search_index'),
        },
    }
    HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

Add the import for the Showroom urls to your ``urls.py`` file and add a ``+`` to the Django admin urls assignment 
to the ``urlpatterns`` list::

    from website_showroom.urls import urlpatterns

    # Before: urlpatterns = [...]
    # After: urlpatterns += [...]

Run Django migration command to create the DB tables and create an admin user::

    python manage.py migrate
    python manage.py createsuperuser

Now run the Django server command::

    python manage runserver

You should be able to enter the Django admin with your user credentials at http://127.0.0.1:8000/admin/.

Example Project
===============
There is an example project where you can see a showroom in action! Go to the ``example_project`` folder of the showroom
lib installation and run a Django server with ``python manage runserver``. Admin credentials are "admin/admin".

