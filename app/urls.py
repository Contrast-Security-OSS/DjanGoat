from django.conf.urls import url, include

from . import views

# import inspect
#
# all_functions = inspect.getmembers(views, inspect.isfunction)
# print(all_functions)

app_name = "app"
print(views.dashboard)


urlpatterns = [
    url(r'^$', views.app_index, name='index'),
    url(r'^dashboard/', include(views.dashboard.urls)),
]
