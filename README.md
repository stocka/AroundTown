# README

## Synopsis

AroundTown is a program for keeping track of what you've been up to around town and how it all went down.  Or something like that.

## Installation

AroundTown uses the [Django](https://www.djangoproject.com/) framework.  

The backend database is SQLite3, the file for which is stored in the `/aroundtown/aroundtown/` folder.  To initialize the database, perform the following command in the `/aroundtown/` folder:

	python manage.py syncdb

Instance-specific settings are stored in a `/aroundtown/aroundtown/local_settings.py` file.  This file must contain a [generated SECRET_KEY value][keygen], in addition to a [Google Maps API key][gmapskey] like so:

	SECRET_KEY = 'secret key goes here'
	GOOGLE_MAPS_API_KEY = 'Google Maps API browser key goes here'

Other, non-required local settings, include [Google Maps map options][gmapsoptions], which can be included like so:

	DEFAULT_MAP_ZOOM = 10
	DEFAULT_MAP_LATITUDE = 39.961176
	DEFAULT_MAP_LONGITUDE = -82.998794

To be able to set up locations and visits, you must create a superuser account.  This can be accomplished through the following command in the `/aroundtown/` folder:

	python manage.py createsuperuser

[keygen]: http://www.miniwebtool.com/django-secret-key-generator/
[gmapskey]: https://developers.google.com/maps/documentation/javascript/tutorial
[gmapsoptions]: https://developers.google.com/maps/documentation/javascript/tutorial#MapOptions
