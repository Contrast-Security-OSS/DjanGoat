from django.conf.urls import include, url

from . import tutorials

urlpatterns = [
    url(r'^$', tutorials.tutorials_credentials, name='tutorials_credentials'),
    url(r'^credentials$', tutorials.tutorials_credentials, name='tutorials_credentials'),
    url(r'^new', tutorials.tutorials_new, name='tutorials_new'),
    url(r'^(?P<id_number>[0-9]+)$', tutorials.tutorials_id, name="tutorials_id"),
    url(r'^(?P<id_number>[0-9]+)/edit$', tutorials.tutorials_id_edit, name="tutorial_edit"),
]
