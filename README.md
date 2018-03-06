# Bucket List API
[![Build Status](https://travis-ci.org/jokamjohn/bucket_api.svg?branch=master)](https://travis-ci.org/jokamjohn/bucket_api)
[![Coverage Status](https://coveralls.io/repos/github/jokamjohn/bucket_api/badge.svg)](https://coveralls.io/github/jokamjohn/bucket_api)
[![BCH compliance](https://bettercodehub.com/edge/badge/jokamjohn/bucket_api?branch=master)](https://bettercodehub.com/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/cfda51ef2f8946639eb34b11fa8b5480)](https://www.codacy.com/app/jokamjohn/bucket_api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jokamjohn/bucket_api&amp;utm_campaign=Badge_Grade)

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

This API is hosted [here](https://warm-wildwood-40594.herokuapp.com/) on [heroku](heroku.com)
## Generating dummy data
You can also generate dummy data to test out the
different API endpoints.
All you have to do is run this command

```
python manage.py dummy
```

A `user` with an email address of `example@bucketmail.com`
and password `123456` is created. And also `100`
Buckets and `1000` Bucket Items are created
and items linked to the different Buckets.

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
