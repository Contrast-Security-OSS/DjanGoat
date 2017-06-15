from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


# -tutorials#index
@require_http_methods(["GET", "POST"])
def index(request):
    return HttpResponse("Welcome to the tutorials!")


# -tutorials#credentials
@require_http_methods(["GET"])
def credentials(request):
    return HttpResponse("Welcome to the tutorial credentials")


# -tutorials#new
@require_http_methods(["GET"])
def new(request):
    return HttpResponse("New tutorial!")


# -tutorials#show, update, destroy
@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
def id(request, id_number):
    return HttpResponse("Welcome tutorial person " + str(id_number))


# -tutorials#edit
@require_http_methods(["GET"])
def id_edit(request, id_number):
    return HttpResponse("Come edit your tutorial person " + str(id_number))
