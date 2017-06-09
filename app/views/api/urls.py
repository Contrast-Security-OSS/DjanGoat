from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.api_index, name='api_index'),
    url(r'^new$', views.api_new, name='api_new'),
    url(r'^(?P<id_number>[0-9]+)/edit$', views.api_id_edit, name='api_id_edit'),
    url(r'^(?P<id_number>[0-9]+)$', views.api_id, name='api_id'),
]

