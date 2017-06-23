from django.conf.urls import url
import views as work_info_views


urlpatterns = [
    url(r'^$', work_info_views.user_work_info_index,
        name="user_work_info_index"),
]
