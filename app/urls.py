from django.conf.urls import include, url
from . import views

app_name = "app"

urlpatterns = [
    url(r'^$', views.app_index, name='index'),
    url(r'^dashboard/', include(views.dashboard.urls)),
    url(r'^tutorials/', include(views.tutorials.urls)),
    url(r'^forgot_password/', views.password_reset_views.forgot_password, name='forgot_password'),
    url(r'^password_resets/', include(views.password_resets.urls))
]
