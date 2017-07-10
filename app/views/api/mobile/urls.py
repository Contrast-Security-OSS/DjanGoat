from django.conf.urls import url

from app.views.api.mobile import views

urlpatterns = [
    url(r'^$', views.api_index, name='api_index'),
    url(r'^(?P<id_number>[0-9]+)$', views.api_id, name='api_id'),
]
