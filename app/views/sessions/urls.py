from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.sessions_index, name='sessions_index'),
]
