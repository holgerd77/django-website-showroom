===========
Development
===========

Release Notes
=============
**Changes in version 0.2** (2015-08-20)

* New organized development structure with new separate docs (this one), branch-based development
* Made ``Haystack`` work again, fixed requirements to ``django-haystack==2.0.0`` and ``Whoosh==2.4.1`` (new
  setting HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor' in ``settings.py`` necessary)
* Replaced ``PIL`` requirement with ``Pillow``
* Support for ``Django 1.8`` (older versions dropped), coming from ``1.4`` following adoptions are necessary:

  * ``ALLOWED_HOSTS`` has to be added to ``settings.py``