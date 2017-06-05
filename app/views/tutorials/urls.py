from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.credentials, name='credentials'),
    url(r'^credentials$', views.credentials, name='credentials'),
    url(r'^new', views.new, name='new'),
    url(r'^(?P<id_number>[0-9]+)$', views.id, name="id"),
    url(r'^(?P<id_number>[0-9]+)/edit$', views.id_edit, name="tutorial_edit"),
]
