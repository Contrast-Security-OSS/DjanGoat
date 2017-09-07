# DjanGoat #

DjanGoat is a vulnerable Django Application based in large part off the [RailsGoat](https://github.com/OWASP/railsgoat) project. The application purports to be an internal employee portal for MetaCorp, Inc but includes vulnerabilities from the [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project) and is intended to be used as an educational tool for developers and security professionals.

## Installation

On a mac, first install python.

### How do I get set up? ###

First, install python and pip. On a mac the easiest solution is to use [Homebrew](https://brew.sh/).

```
    brew install python
```


Next, install virtual-env
```
    pip install virtualenv
```

Begin by creating a virtual-env
```
    virtualenv env
    source env/bin/activate
```

Then install using pip
```
    pip install -r requirements.txt
```

### DB-Setup ###

Now we need to setup our database
1. Install [PostgreSQL](https://www.postgresql.org/download/). 
Please note the host and port number during installation so they can 
be set in your production_settings.py file. To make sure PostgreSQL is 
setup properly follow these steps:
   
   a) Run `pg_config` in terminal.
    
   b) If you get a not found error, run `sudo find / -name pg_config`. 
   There should be a path of the form 'Library/PostgreSQL/9.5/bin/pg_profile'
   
   c) Add the path, minus the '/pg_profile' to .bash_profile in your home directory
   `export PATH=/Library/PostgreSQL/9.5/bin:$PATH`. Make sure to replace this with your appropriate path
   
   d) Restart terminal, then run `pg_config` again to make sure it is properly working
   
2. Setup the database

```
    $ psql -U postgres
    postgres=# CREATE DATABASE djangoat;
    postgres=# \c djangoat
    djangoat=# CREATE USER your_username WITH BY 'your_password';
    djangoat=# GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO your_username;
    djangoat=# \q
```

3. Go to production_settings.py in the inner pygoat folder and fill out the given information
   for your database. Make sure that host and port number are filled out, as they are not required for mysql

4. Migrate the models and associated database data

```
    python manage.py makemigrations
    python manage.py migrate
```

5. To set up seed data you can run:

```
    python manage.py seed
```

For developers create a local_settings.py file in the pygoat folder
that mocks production_setting.py.

Finally run on localhost:8000
```
    python manage.py runserver
```

### Testing ###
To run tests, simply run:
```
    python manage.py test app
```

### Linting ###

To run the `pylint` before running on Jenkins, run:

```
pylint app pygoat
```

### Docker ###
For Docker when you're testing locally make sure you give executable
permissions to build.sh by running
```
chmod +x build.sh
```

## Tutorial ##
Tutorial information on the various vulnerabilities in this application are [here](docs/home.md).

## Acknowledgements ##
The development [team](docs/acknowledgements.md).