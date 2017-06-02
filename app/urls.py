from django.conf.urls import url

from . import views

app_name = "app"

urlpatterns = [
    url(r'^$', views.app_index, name='index'),
    url(r'^dashboard/$', views.dashboard_index, name='dashboard'),
    url(r'^dashboard/home$', views.dashboard_home, name='dashboard home'),
    url(r'^dashboard/doc$', views.dashboard_doc, name='dashboard doc'),
    url(r'^dashboard/change_graph$', views.dashboard_change_graph, name='dashboard change graph'),
    url(r'^dashboard/new$', views.dashboard_new, name='dashboard new'),
    url(r'^dashboard/(?P<dashboard_id>[0-9]+)/edit$', views.dashboard_edit, name="dashboard edit"),
    url(r'^dashboard/(?P<dashboard_id>[0-9]+)$', views.dashboard, name="dashboard"),

]
