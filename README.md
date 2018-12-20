[![Build Status](https://travis-ci.org/Contrast-Security-OSS/DjanGoat.svg?branch=master)](https://travis-ci.org/Contrast-Security-OSS/DjanGoat)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6116741df83d465d975c94e42d3f3163)](https://app.codacy.com/app/SteveFeldman/DjanGoat?utm_source=github.com&utm_medium=referral&utm_content=Contrast-Security-OSS/DjanGoat&utm_campaign=Badge_Grade_Settings)
[![CodeFactor](https://www.codefactor.io/repository/github/contrast-security-oss/djangoat/badge)](https://www.codefactor.io/repository/github/contrast-security-oss/djangoat)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/Contrast-Security-OSS/DjanGoat.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Contrast-Security-OSS/DjanGoat/alerts/)
<a href="https://codeclimate.com/github/Contrast-Security-OSS/DjanGoat/maintainability"><img src="https://api.codeclimate.com/v1/badges/12031df53865b695f317/maintainability" /></a>
[![codebeat badge](https://codebeat.co/badges/cced60a6-7204-44a6-94df-68ae676b719d)](https://codebeat.co/projects/github-com-contrast-security-oss-djangoat-master)

# DjanGoat

DjanGoat is a vulnerable Django Application based in large part off the [RailsGoat](https://github.com/OWASP/railsgoat) project. The application purports to be an internal employee portal for MetaCorp, Inc but includes vulnerabilities from the [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project) and is intended to be used as an educational tool for developers and security professionals. 

## Installation

On a mac, first install python.

### How do I get set up?

Requirements:

 - Python 2.7
 - Pip
 - mysql (optional)

Begin by creating a virtual-env
```
    pip install virtualenv
    virtualenv env
    source env/bin/activate
```

Then install using pip
```
    pip install -r requirements.txt
```

### DB-Setup

#### SQLite:
   
   Djangoat uses a SQLite database by default.

#### MySQL & PostgreSQL
If you want to use a MySQL database, continue following this README. 
If you want to setup DjanGoat with a PostgreSQL database, checkout the PostgreSQL branch with the following command:
```
$ git checkout postgresql-database
```
The PostgreSQL branch has modified documentation and tests.

1. Make sure you have mysql installed and run the following to
setup the database

```
    mysql -u root -p
    CREATE DATABASE `db_name`;
    CREATE USER 'username'@'localhost' IDENTIFIED BY 'your_password';
    GRANT ALL PRIVILEGES ON `db_name`.* TO 'username'@'localhost';
    FLUSH PRIVILEGES;
    quit
```

2. Go to pygoat/production_settings.py and fill out the given information for your database.

3. Migrate the models and associated database data

```
    python manage.py makemigrations
    python manage.py migrate
```

4. To set up seed data you can run:

```
    python manage.py seed
```

For developers create a local_settings.py file in the pygoat folder
that mocks production_setting.py.

If Django does not recognize MySQL after the setup above, try install mysql-python and migrate again

```
    pip install mysql-python
```

Finally run on localhost:8000
```
    python manage.py runserver
```

### Testing
To run tests, simply run:
```
    python manage.py test app
```

### Linting

To run the `pylint` before running on Jenkins, run:
```
pylint app pygoat
```

## Tutorial
Tutorial information on the various vulnerabilities in this application are [here](docs/home.md).

## Acknowledgements
The development [team](docs/acknowledgements.md).
