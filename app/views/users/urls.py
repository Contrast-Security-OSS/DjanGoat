from django.conf.urls import url, include
from app.views.users import views as users_views
from app.views.users.messages import urls as messages
from app.views.users.benefit_forms import urls as benefit_forms
from app.views.users.retirement import urls as retirement
from app.views.users.pay import urls as pay
from app.views.users.work_info import urls as work_info
from app.views.users.paid_time_off import urls as paid_time_off
from app.views.users.performance import urls as performance

urlpatterns = [
    url(r'^$', users_views.index, name='users_index'),
    url(r'^(?P<user_id>[0-9]+)/account_settings$',
        users_views.account_settings, name="user_account_settings"),
    url(r'^(?P<user_id>[0-9]+)$', users_views.user_view, name="user_view"),
    url(r'^(?P<user_id>[0-9]+)/messages/', include(messages)),
    url(r'^(?P<user_id>[0-9]+)/messages.json', include(messages)),
    url(r'^(?P<user_id>[0-9]+)/benefit_forms/', include(benefit_forms)),
    url(r'^(?P<user_id>[0-9]+)/work_info/', include(work_info)),
    url(r'^(?P<user_id>[0-9]+)/retirement/', include(retirement)),
    url(r'^(?P<user_id>[0-9]+)/pay/', include(pay)),
    url(r'^(?P<user_id>[0-9]+)/paid_time_off/', include(paid_time_off)),
    url(r'^(?P<user_id>[0-9]+)/performance/', include(performance)),
]
