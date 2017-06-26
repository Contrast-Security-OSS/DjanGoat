from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<selected_id>[0-9]+)/dashboard/$', views.admin_dashboard, name='admin_dashboard'),
    url(r'^(?P<selected_id>[0-9]+)/get_user/$', views.admin_get_user, name='admin_get_user'),
    url(r'^(?P<selected_id>[0-9]+)/delete_user/$', views.admin_delete_user, name='admin_delete_user'),
    url(r'^(?P<selected_id>[0-9]+)/update_user/$', views.admin_update_user, name='admin_update_user'),
    url(r'^(?P<selected_id>[0-9]+)/get_all_users/$', views.admin_get_all_users, name='admin_get_all_users'),
    url(r'^(?P<selected_id>[0-9]+)/analytics/$', views.admin_analytics, name='admin_analytics'),
]
