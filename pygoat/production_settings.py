import os
import dj_database_url

connection_string = os.environ.get('MYSQL_HOST', None)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
