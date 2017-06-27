from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='pto_index'),
    url(r'^new', views.new, name='pto_new'),
    url(r'^(?P<id>[0-9])+/edit$', views.edit, name='pto_edit'),
    url(r'^(?P<id>[0-9])+', views.pto_id, name='pto_id'),
]
