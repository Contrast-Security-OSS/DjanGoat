from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from app.decorators import user_is_authenticated
from app.views import utils


@require_http_methods(["GET"])
@user_is_authenticated
def home(request):
    current_user = utils.current_user(request)
    context = {'current_user': current_user}
    return render(request, 'dashboard/home.html', context=context)


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
@user_is_authenticated
def dashboard_view(request, dashboard_id):
    return HttpResponse("Dashboard " + str(dashboard_id))
