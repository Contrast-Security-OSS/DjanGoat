from django.conf.urls import url
import app.views.users.paid_time_off.views as views


urlpatterns = [
    url(r'^$', views.index, name='pto_index'),
]
