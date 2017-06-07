from django.conf.urls import url
import views as schedule_views


urlpatterns = [
    url(r'^$', schedule_views.schedule_index, name='schedule_index'),
    url(r'^get_pto_schedule$', schedule_views.get_pto_schedule_schedule_index,
        name='get_pto_schedule_schedule_index'),
    url(r'^new$', schedule_views.new_schedule, name='new_schedule'),
    url(r'^(?P<schedule_id>[0-9]+)/edit$', schedule_views.edit_schedule,
        name='edit_schedule'),
    url(r'^(?P<schedule_id>[0-9]+)$', schedule_views.schedule,
        name='schedule'),
]
