"""
WSGI config for 'pygoat' project.

It exposes the WSGI callable as a module-level variable named `application`.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from caduceus.wsgi import Caduceus
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pygoat.settings")

caduceus_project_id = "4f907b1c-2104-490e-bf46-293f11d24162"
application = Caduceus(get_wsgi_application(), caduceus_project_id)
