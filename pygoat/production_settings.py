import os
import dj_database_url

connection_string = os.environ.get('MYSQL_HOST', None)

if not connection_string:
    print('NO CONNECTION STRINGGGGG')

DATABASES = {
    'default': dj_database_url.parse(connection_string, conn_max_age=600)
}
