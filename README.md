# Pygoat #



### How do I get set up? ###

First, install virtual-env
```
    pip install virtualenv
```

Begin by creating a virtual-env
```
    virutalenv env
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
CREATE DATABASE 'db_name';
CREATE USER 'username'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON 'db_name'.* TO 'username'@'localhost';
FLUSH PRIVILEGES;
quit
```

2. Go to production_settings.py and fill out the given information
   for your database.

3. ```
    python manage.py makemigrations
    python manage.py migrate
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
