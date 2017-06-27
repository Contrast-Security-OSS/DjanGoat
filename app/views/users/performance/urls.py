from django.conf.urls import url
from . import views as performance_views

urlpatterns = [
    url(r'^$', performance_views.user_performance_index,
        name="user_performance_index")
]
