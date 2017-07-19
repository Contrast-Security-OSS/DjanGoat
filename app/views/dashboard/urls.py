from django.conf.urls import url
from . import views as dashboard_views


urlpatterns = [
    url(r'^home$', dashboard_views.home, name='dashboard_home'),
    url(r'^(?P<dashboard_id>[0-9]+)$', dashboard_views.dashboard_view,
        name="dashboard_view"),
]
