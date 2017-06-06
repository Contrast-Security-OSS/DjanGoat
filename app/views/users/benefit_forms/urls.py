from django.conf.urls import url
import views as benefit_forms_views


urlpatterns = [
    url(r'^$', benefit_forms_views.user_benefit_forms, name="user_benefit_forms"),
    url(r'^new$', benefit_forms_views.new_user_benefit_form, name="new_user_benefit_form"),
    url(r'^(?P<benefit_form_id>[0-9]+)/edit$', benefit_forms_views.edit_user_benefit_form, name="edit_user_benefit_form"),
    # url(r'^(?P<message_id>[0-9]+)$', benefit_forms_views.user_benefit_forms, name="user_benefit_forms"),
]
