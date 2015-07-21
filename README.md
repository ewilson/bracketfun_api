[![Build Status](https://travis-ci.org/ewilson/titlematch_api.svg?branch=serialization)](https://travis-ci.org/ewilson/titlematch_api)

TitleMatch API
==============

Python/Django API for TitleMatch applications. This will serve the [TitleMatch web](https://github.com/ewilson/titlematch_web) client. A more detailed README is maintained at that repo.

### Local development setup

TitleMatch uses Python 3.4

To install dependencies:

    $ pip install -r requirements.txt

To run locally:

    $ ./manage.py runserver

or better, install Postgres and Heroku, and use:

    $ foreman start

To run tests:

    $ ./manage.py test
