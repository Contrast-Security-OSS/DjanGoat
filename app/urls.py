from django.conf.urls import include, url

from . import views

app_name = "app"

urlpatterns = [
    url(r'^$', views.app_index, name='index'),
    url(r'^dashboard/$', views.dashboard_home, name='dashboard'),
    url(r'^tutorials/', include(views.tutorial_urls)),
]
