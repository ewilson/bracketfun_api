[![Build Status](https://travis-ci.org/ewilson/titlematch_api.svg?branch=serialization)](https://travis-ci.org/ewilson/titlematch_api)

BracketFun API
==============

Python/Django API for the BracketFun web application.
This will serve the [BracketFun web](https://github.com/ewilson/titlematch_web) client. 
The README.md in that that repo is more interesting.

### Local development setup

BracketFun-API uses Python 3.4

To install dependencies:

    $ pip install -r requirements.txt

#### Postgres setup

1. Install Postgres
1. Create user `bracket_app` with password `bracket_pass`
1. Create database `bracketfun`
1. `DATABASE_URL=postgres://bracket_app:bracket_pass@localhost:5432/bracketfun`
1. Use `./manage makemigrations tournament` and `./manage migrate` to create DB tables

To reset DB on Heroku (drops tables):

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
