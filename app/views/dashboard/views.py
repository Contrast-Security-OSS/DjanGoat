from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.template.loader import get_template

from app.decorators import user_is_authenticated


@require_http_methods(["GET", "POST"])
@user_is_authenticated
def index(request):
    return HttpResponse("dashboard index")


@require_http_methods(["GET"])
@user_is_authenticated
def home(request):
    t = get_template('dashboard/home.html')
    html = t.render()
    return HttpResponse(html)


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
