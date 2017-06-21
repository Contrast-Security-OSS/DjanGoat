from django.conf.urls import url
import views as messages_views


urlpatterns = [
    url(r'^$', messages_views.user_messages, name="user_messages"),
    url(r'^(?P<message_id>[0-9]+)$', messages_views.user_message,
        name="user_message")
]
