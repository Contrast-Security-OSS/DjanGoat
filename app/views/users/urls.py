from django.conf.urls import url
import views as users_views


urlpatterns = [
    url(r'^$', users_views.index, name='users_index'),
    url(r'^new$', users_views.new_user, name='users_new'),
    url(r'^(?P<user_id>[0-9]+)/edit$', users_views.edit_user, name="user_edit"),
    url(r'^(?P<user_id>[0-9]+)/account_settings$', users_views.account_settings, name="user_account_settings"),
    url(r'^(?P<user_id>[0-9]+)$', users_views.user_view, name="user_view"),

]
