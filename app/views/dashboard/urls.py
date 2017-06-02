from django.conf.urls import url
import dashboard as d


urlpatterns = [
    url(r'^dashboard/$', d.index, name='dashboard'),
    url(r'^dashboard/home$', d.home, name='dashboard home'),
    url(r'^dashboard/doc$', d.doc, name='dashboard doc'),
    url(r'^dashboard/change_graph$', d.change_graph, name='dashboard change graph'),
    url(r'^dashboard/new$', d.new_dashboard, name='dashboard new'),
    url(r'^dashboard/(?P<dashboard_id>[0-9]+)/edit$', d.edit_dashboard, name="dashboard edit"),
    url(r'^dashboard/(?P<dashboard_id>[0-9]+)$', d.dashboard, name="dashboard"),
]
