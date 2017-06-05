from django.conf.urls import url
import views as d


urlpatterns = [
    url(r'^$', d.index, name='dashboard_index'),
    url(r'^home$', d.home, name='dashboard_home'),
    url(r'^doc$', d.doc, name='dashboard_doc'),
    url(r'^change_graph$', d.change_graph, name='dashboard_change_graph'),
    url(r'^new$', d.new_dashboard, name='dashboard_new'),
    url(r'^(?P<dashboard_id>[0-9]+)/edit$', d.edit_dashboard, name="dashboard_edit"),
    url(r'^(?P<dashboard_id>[0-9]+)$', d.dashboard_view, name="dashboard_view"),
]
