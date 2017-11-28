from django.conf.urls import url
from app.views.users.retirement import views as retirement_views

urlpatterns = [
    url(r'^$', retirement_views.user_retirement_index,
        name="user_retirement_index")
]
