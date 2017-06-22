from django.conf.urls import url
import views as benefit_forms_views


urlpatterns = [
    url(r'^$', benefit_forms_views.user_benefit_forms,
        name="user_benefit_forms"),
]
