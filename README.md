# Pygoat #

### DB-Setup ###

For developers create a local_settings.py file in the pygoat folder
that mocks production_setting.py.

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

Finally run on localhost:8000
```
    python manage.py runserver
```




### Testing ###
To run tests, simply run:
```
  python manage.py test app
```
