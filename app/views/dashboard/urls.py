from django.conf.urls import url
from . import views as dashboard_views


urlpatterns = [
    url(r'^$', dashboard_views.index, name='dashboard_index'),
    url(r'^home$', dashboard_views.home, name='dashboard_home'),
    url(r'^doc$', dashboard_views.doc, name='dashboard_doc'),
    url(r'^change_graph$', dashboard_views.change_graph,
        name='dashboard_change_graph'),
    url(r'^new$', dashboard_views.new_dashboard, name='dashboard_new'),
    url(r'^(?P<dashboard_id>[0-9]+)/edit$', dashboard_views.edit_dashboard,
        name="dashboard_edit"),
    url(r'^(?P<dashboard_id>[0-9]+)$', dashboard_views.dashboard_view,
        name="dashboard_view"),
]
