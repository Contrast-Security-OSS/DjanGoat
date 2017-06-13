from django.conf.urls import url
import views as performance_views

urlpatterns = [
    url(r'^$', performance_views.user_performance_index,
        name="user_performance_index"),
    url(r'^new$', performance_views.new_user_performance,
        name="new_user_performance"),
    url(r'^(?P<performance_id>[0-9]+)/edit$',
        performance_views.edit_user_performance,
        name="edit_user_performance"),
    url(r'^(?P<performance_id>[0-9]+)$',
        performance_views.user_performance,
        name="user_performance"),
]
