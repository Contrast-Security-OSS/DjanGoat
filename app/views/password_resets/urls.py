from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.reset_password_handler, name='password_resets'),
]
