from __future__ import unicode_literals

from index import index as app_index

from dashboard import views as dashboard_views
from tutorials import views as tutorials_views
from password_resets import views as password_reset_views
from users import views as users_views
from users.messages import views as user_messages_views
from users.benefit_forms import views as user_benefit_forms_views
from users.work_info import views as user_work_info_views
from users.retirement import views as user_retirement_views
from sessions import views as sessions_views
from schedule import views as schedule_views
from api import views as api_views
from users.pay import views as user_messages_pay
from users.paid_time_off import views as pto_views
from users.performance import views as user_performance_views
from admin import views as admin_views