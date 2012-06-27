Website Showroom
================

Python/Django project to easily create showroom websites presenting different websites around a certain topic, originally used for http://opendata-tools.org (engl.) and http://opendata-showroom.org (german).

Features
--------
- Administrable via Django admin (Categories, Websites)
- Automatic screenshot resize
- Customizable category colors
- Things like title, subtitle, footer configurable via settings.py
- No language dependent static code

Requirements
------------
- Python v.2.x (Tested on 2.7, 2.6 should work)
- Django v.1.4
- django-haystack v.2.0 (Search module for Django)
- PIL
- Whoosh v.2.4.1 (Full-text search enginge used for django-haystack)
- django-debug-toolbar (optional, if you don't have it installed, comment out "debug_toolbar" in INSTALLED_APPS in settings.py)

Installation/Setup
------------------
- Install requirement libraries from above, probably most easy in a virtualenv environment
- Install showroom sources from GitHub
- Create your project, add ''website_showroom'' as an app
- Customize your site's title, subtitle,... via settings.py (see opendata-showroom-org GitHub project as example)
- Create desired categories, websites via admin interface
