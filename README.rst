DJANGO-NOSE-ROLLBACK
====================

A simple plugin for Nose that performs a rollback on your Django database after
each test.

Description
-----------

Django-nose-rollback is enabled once it is installed.

To disable it, once the plugin is installed, use either the command line::

    --without-django-rollback

or, set add it in your ``settings.py``::

    NOSE_ARGS = ['--without-django-rollback']

Install
-------

This package is not yet on PyPI so you'll have to install it manually or add it
to your buildout package (and use the gp.vcsdevelop extension for example).
