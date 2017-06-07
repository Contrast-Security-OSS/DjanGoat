from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pygoat',
        'USER': 'pygoat',
        'PASSWORD': 'default1!',
        'HOST': '',  # can leave blank (sets to default)
        'PORT': '',  # can leave blank (sets to default)
    }
}