# congenial-happiness
A Python/Flask project by The Midnight Jackals

[![Build Status](https://travis-ci.org/danphill01/congenial-happiness.svg?branch=master)](https://travis-ci.org/danphill01/congenial-happiness)
[![Coverage Status](https://coveralls.io/repos/github/danphill01/congenial-happiness/badge.svg?branch=master)](https://coveralls.io/github/danphill01/congenial-happiness?

## Usage
- [Running the application](#starting-the-application)
- [Live Application](#live-application)
- [Generating Dummy Data](#generating-dummy-data)
- [Running tests](#running-tests)


## Starting the application
In order to run the application set the environment
variable below.
```
Windows
set FLASK_APP=run.py

Unix
export FLASK_APP=run.py
```
Then run the command below to start the application.
```
flask run
```

## Live Application

This app is hosted [here](https://warm-wildwood-40594.herokuapp.com/) on [heroku](heroku.com)
## Generating dummy data
You can also generate dummy data to test out the
different API endpoints.
All you have to do is run this command

```
python manage.py dummy
```

A `user` with an email address of `user@email.com`
and password `123456` is created. And also `100`
series and `1000` events are created
and events linked to the different series.

## Running tests
Before running the application tests, update your env variables
```
export  APP_SETTINGS=app.config.TestingConfig
export DATABASE_URL_TEST=<postgres database url>
```

### Running tests without coverage
You can now run the tests from the terminal
```
python manage.py test
```

### Running tests with coverage
You can also run tests with coverage by running this command in the terminal
```
nosetests --with-coverage --cover-package=app
```
=======
