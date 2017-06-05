from django.conf.urls import include, url
from . import views

app_name = "app"


urlpatterns = [
    url(r'^$', views.app_index, name='index'),
    url(r'^dashboard/', include(views.dashboard.urls)),
    url(r'^tutorials/', include(views.tutorials.urls)),
    url(r'^users/', include(views.users.urls)),
    url(r'^signup/', views.users_views.signup, name='user_signup'),
]
