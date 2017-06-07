from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.sessions_index, name='sessions_index'),
    url(r'^new$', views.new_sessions, name='sessions_new'),
    url(r'^(?P<id_number>[0-9]+)/edit$', views.edit_session, name='sessions_edit'),
    url(r'^(?P<id_number>[0-9]+)', views.session_id, name='session_id'),
]
