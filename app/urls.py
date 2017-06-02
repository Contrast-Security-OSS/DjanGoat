from django.conf.urls import url

from . import views

app_name = "app"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/$', views.home, name='dashboard'),
]
