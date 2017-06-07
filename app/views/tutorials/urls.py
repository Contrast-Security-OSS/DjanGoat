from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='tutorials_index'),
    url(r'^credentials$', views.credentials, name='tutorials_credentials'),
    url(r'^new', views.new, name='tutorials_new'),
    url(r'^(?P<id_number>[0-9]+)$', views.id, name="tutorials_id"),
    url(r'^(?P<id_number>[0-9]+)/edit$', views.id_edit,
        name="tutorials_id_edit"),
]
