from django.conf.urls import url, include
import app.views.users.views as users_views
import app.views.users.messages.views as messages
import app.views.users.benefit_forms.views as benefit_forms
import app.views.users.retirement.views as retirement
import app.views.users.pay.views as pay
import app.views.users.work_info.views as work_info
import app.views.users.paid_time_off.views as paid_time_off
import app.views.users.performance.views as performance

urlpatterns = [
    url(r'^$', users_views.index, name='users_index'),
    url(r'^(?P<user_id>[0-9]+)/account_settings$',
        users_views.account_settings, name="user_account_settings"),
    url(r'^(?P<user_id>[0-9]+)$', users_views.user_view, name="user_view"),
    url(r'^(?P<user_id>[0-9]+)/messages/', include(messages.urls)),
    url(r'^(?P<user_id>[0-9]+)/messages.json', include(messages.urls)),
    url(r'^(?P<user_id>[0-9]+)/benefit_forms/', include(benefit_forms.urls)),
    url(r'^(?P<user_id>[0-9]+)/work_info/', include(work_info.urls)),
    url(r'^(?P<user_id>[0-9]+)/retirement/', include(retirement.urls)),
    url(r'^(?P<user_id>[0-9]+)/pay/', include(pay.urls)),
    url(r'^(?P<user_id>[0-9]+)/paid_time_off/', include(paid_time_off.urls)),
    url(r'^(?P<user_id>[0-9]+)/performance/', include(performance.urls)),
]
