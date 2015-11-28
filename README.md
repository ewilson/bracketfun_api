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
1. `export DATABASE_URL='postgres://tma:tma_pass@localhost:5432/titlematch'`
1. Use `./manage migrate` to create DB tables

To reset DB on Heroku:

    $ heroku pg:reset --app secure-badlands-8145 DATABASE

To reset DB locally:

    $ ./manaage.py flush
    
#### Heroku setup

You should be able to run with `./manage.py runserver`, but it is better to use Heroku locally, to 
minimize differences between dev and production.

To run locally, install Heroku toolbelt, and use:

    $ heroku local

To run tests:

    $ ./manage.py test
