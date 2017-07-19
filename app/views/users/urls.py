from django.conf.urls import url, include
from . import views as users_views
from . import messages
from . import benefit_forms
from . import retirement
from . import pay
from . import work_info
from . import paid_time_off
from . import performance

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
