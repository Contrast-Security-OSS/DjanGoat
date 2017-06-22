from django.conf.urls import url

from app.views.api.users import views

urlpatterns = [
    url(r'^$', views.api_index, name='api_users_index'),
    url(r'^(?P<id_number>[0-9]+)$', views.api, name='api_users_id'),
]

