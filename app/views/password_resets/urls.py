from django.conf.urls import url
import views as password_reset_views


urlpatterns = {
    url(r'^$', password_reset_views.reset_password, name='forgot_password'),
}
