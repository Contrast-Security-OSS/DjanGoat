from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.template.loader import get_template
from django.shortcuts import render
from app.decorators import user_is_authenticated
from app.views import utils


@require_http_methods(["GET", "POST"])
@user_is_authenticated
def index(request):
    return HttpResponse("dashboard index")


@require_http_methods(["GET"])
@user_is_authenticated
def home(request):
    user = utils.current_user(request)
    return render(request, 'dashboard/home.html',
                  context={'current_user': user})


@require_http_methods(["GET"])
@user_is_authenticated
def doc(request):
    return HttpResponse("dashboard doc")


@require_http_methods(["GET"])
@user_is_authenticated
def change_graph(request):
    return HttpResponse("Change Graph Index")


@require_http_methods(["GET"])
@user_is_authenticated
def new_dashboard(request):
    return HttpResponse("New dashboard")


@require_http_methods(["GET"])
@user_is_authenticated
def edit_dashboard(request, dashboard_id):
    return HttpResponse("Edit dashboard " + str(dashboard_id))


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
@user_is_authenticated
def dashboard_view(request, dashboard_id):
    return HttpResponse("Dashboard " + str(dashboard_id))
