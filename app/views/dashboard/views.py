from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods



@require_http_methods(["GET", "POST"])
def index(request):
    return HttpResponse("dashboard index")

@require_http_methods(["GET"])
def home(request):
    return HttpResponse("dashboard home index")

@require_http_methods(["GET"])
def doc(request):
    return HttpResponse("dashboard doc")

@require_http_methods(["GET"])
def change_graph(request):
    return HttpResponse("Change Graph Index")

@require_http_methods(["GET"])
def new_dashboard(request):
    return HttpResponse("New dashboard")

@require_http_methods(["GET"])
def edit_dashboard(request, dashboard_id):
    return HttpResponse("Edit dashboard " + str(dashboard_id))

@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
def dashboard_view(request, dashboard_id):
    return HttpResponse("Dashboard " + str(dashboard_id) + " " + str(request.method))
