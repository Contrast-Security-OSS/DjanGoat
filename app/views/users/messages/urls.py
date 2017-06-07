from django.conf.urls import url
import views as messages_views


urlpatterns = [
    url(r'^$', messages_views.user_messages, name="user_messages"),
    url(r'^new$', messages_views.new_user_message, name="new_user_message"),
    url(r'^(?P<message_id>[0-9]+)/edit$', messages_views.edit_user_message,
        name="edit_user_message"),
    url(r'^(?P<message_id>[0-9]+)$', messages_views.user_message,
        name="user_message"),
]
