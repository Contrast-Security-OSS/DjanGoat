from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.user_pay_index, name='pay_index'),
    url(r'^update_dd_info', views.update_dd_info, name='update_dd_info'),
    url(r'^decrypted_bank_acct_num', views.decrypt_bank_acct_num,
        name='decrypted_bank_acct_num'),
    url(r'^new', views.new_user_pay, name='pay_new'),
    url(r'^(?P<id>[0-9]+)/edit', views.edit_user_pay, name='pay_edit'),
    url(r'^(?P<id>[0-9]+)', views.user_pay, name='pay_user')
]
