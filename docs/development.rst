===========
Development
===========

Release Notes
=============
**Changes in version 0.3** (2015-08-24)

* TODO

**Changes in version 0.2** (2015-08-20)

* New organized development structure with new separate docs (this one), branch-based development
* Made ``Haystack`` work again, fixed requirements to ``django-haystack==2.0.0`` and ``Whoosh==2.4.1`` (new
  setting HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor' in ``settings.py`` necessary)
* Replaced ``PIL`` requirement with ``Pillow``
* Support for ``Django 1.8`` (older versions dropped), coming from ``1.4`` following adoptions are necessary:

  * ``ALLOWED_HOSTS`` has to be added to ``settings.py`` of Django project
  * ``python manage.py migrate`` has to be run to apply/recognize the new ``Django`` migrations

* Replaced ``South`` migrations with re-generated ``Django`` internal migrations
* Setup instructions in docs
* New ``example_project`` Django project with basic Color Website Showroom example
* Section in docs describing how to create a showroom website
* Fixed some bugs

**Changes in version 0.1** (A long time ago...)

* Initial version, just existing in ``master`` branch, no dedicated ``tags`` or ``pip`` releases yet
