from django.conf.urls import url
from app.views.users.paid_time_off import views as views


urlpatterns = [
    url(r'^$', views.index, name='pto_index'),
]
