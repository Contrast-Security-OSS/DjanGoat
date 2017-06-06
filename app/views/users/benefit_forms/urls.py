from django.conf.urls import url
import views as benefit_forms_views


urlpatterns = [
    url(r'^$', benefit_forms_views.user_benefit_forms, name="user_benefit_forms"),
    # url(r'^new$', messages_views.new_user_message, name="new_user_message"),
    # url(r'^(?P<message_id>[0-9]+)/edit$', messages_views.edit_user_message, name="edit_user_message"),
    # url(r'^(?P<message_id>[0-9]+)$', messages_views.user_message, name="user_message"),
]
