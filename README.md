[![Build Status](https://travis-ci.org/ewilson/titlematch_api.svg?branch=serialization)](https://travis-ci.org/ewilson/titlematch_api)

TitleMatch API
==============

Python/Django API for the TitleMatch web application.
This will serve the [TitleMatch web](https://github.com/ewilson/titlematch_web) client. 
The README.md in that that repo is more interesting.

### Local development setup

TitleMatch uses Python 3.4

To install dependencies:

    $ pip install -r requirements.txt

#### Postgres setup

1. Install Postgres
1. Create user `tma` with password `tma_pass`
1. Create database `titlematch`
1. Grant privileges to `tma` for `titlematch`
1. Use `./manage migrate` to create DB tables

#### Heroku setup

This application is setup for use with Heroku, so `./manage.py runserver` will not detect the DB engine.

To run locally, install Heroku toolbelt, and use:

    $ heroku local

To run tests:

    $ ./manage.py test
