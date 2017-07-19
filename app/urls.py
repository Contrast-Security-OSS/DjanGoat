from django.conf.urls import include, url
from django.views.generic import RedirectView
from . import views

app_name = "app"

# url(r'^$', RedirectView.as_view(pattern_name='dashboard_home', permanent=False), name='index'),
urlpatterns = [
    url(r'^$', RedirectView.as_view(url='dashboard/home', permanent=False)),
    url(r'^dashboard/', include(views.dashboard.urls)),
    url(r'^forgot_password/', views.password_reset_views.forgot_password, name='forgot_password'),
    url(r'^password_resets/', include(views.password_resets.urls)),
    url(r'^users/', include(views.users.urls)),
    url(r'^signup/', views.users_views.signup, name='user_signup'),
    url(r'^upload/', views.user_benefit_forms_views.upload, name='upload_benefit_form'),
    url(r'^download/', views.user_benefit_forms_views.download, name='download_benefit_form'),
    url(r'^login/', views.sessions_views.login, name='login'),
    url(r'^logout/', views.sessions_views.logout, name='logout'),
    url(r'^sessions/', include(views.sessions.urls)),
    url(r'^api/v1/mobile/', include(views.api.mobile.urls)),
    url(r'^api/v1/users/', include(views.api.users.urls)),
    url(r'^admin/', include(views.admin.urls))
]
