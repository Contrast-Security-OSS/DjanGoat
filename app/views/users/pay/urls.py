from django.conf.urls import url
from app.views.users.pay import views as views

urlpatterns = [
    url(r'^$', views.user_pay_index, name='pay_index'),
    url(r'^update_dd_info', views.update_dd_info, name='update_dd_info'),
    url(r'^decrypt_bank_account_num', views.decrypt_bank_acct_num,
        name='decrypt_bank_acct_num'),
    url(r'^(?P<pay_id>[0-9]+)', views.user_pay, name='pay_user')
]
