from django.conf.urls import url
import views as retirement_views


urlpatterns = [
    url(r'^$', retirement_views.user_retirement_index, name="user_retirement_index"),
    url(r'^new$', retirement_views.new_user_retirement, name="new_user_retirement"),
    url(r'^(?P<retirement_id>[0-9]+)/edit$', retirement_views.edit_user_retirement, name="edit_user_retirement"),
    # url(r'^(?P<message_id>[0-9]+)$', retirement_views.user_retirement, name="user_retirement"),
]
