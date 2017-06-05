from django.conf.urls import url
import views as d


urlpatterns = [
    url(r'^$', d.index, name='dashboard'),
    url(r'^home$', d.home, name='dashboard home'),
    url(r'^doc$', d.doc, name='dashboard doc'),
    url(r'^change_graph$', d.change_graph, name='dashboard change graph'),
    url(r'^new$', d.new_dashboard, name='dashboard new'),
    url(r'^(?P<dashboard_id>[0-9]+)/edit$', d.edit_dashboard, name="dashboard edit"),
    url(r'^(?P<dashboard_id>[0-9]+)$', d.dashboard, name="dashboard"),
]
