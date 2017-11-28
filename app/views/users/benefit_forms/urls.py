from django.conf.urls import url
from app.views.users.benefit_forms import views as benefit_forms_views

urlpatterns = [
    url(r'^$', benefit_forms_views.user_benefit_forms,
        name="user_benefit_forms"),
]
