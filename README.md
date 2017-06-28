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

2. Go to production_settings.py in the inner pygoat folder and fill out the given information
   for your database.

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
