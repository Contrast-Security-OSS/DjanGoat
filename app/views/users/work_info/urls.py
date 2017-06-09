from django.conf.urls import url
import views as work_info_forms_views


urlpatterns = [
    url(r'^$', work_info_forms_views.user_work_info_index,
        name="user_work_info_index"),
    url(r'^new$', work_info_forms_views.new_user_work_info,
        name="new_user_work_info"),
    url(r'^(?P<work_info_id>[0-9]+)/edit$',
        work_info_forms_views.edit_user_work_info,
        name="edit_user_benefit_form"),
    url(r'^(?P<work_info_id>[0-9]+)$',
        work_info_forms_views.user_work_info,
        name="user_work_info"),
]
