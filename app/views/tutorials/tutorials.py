from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


# -tutorials#index
@require_http_methods(["GET", "POST"])
def tutorials_index(request):
    return HttpResponse("Welcome to the tutorials!")


# -tutorials#credentials
@require_http_methods(["GET"])
def tutorials_credentials(request):
    return HttpResponse("Welcome to the tutorial credentials")


# -tutorials#new
@require_http_methods(["GET"])
def tutorials_new(request):
    return HttpResponse("New tutorial!")


# -tutorials#show, update, destroy
@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
def tutorials_id(request, id_number):
    return HttpResponse("Welcome tutorial person " + id_number)


# -tutorials#edit
@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
def tutorials_id_edit(request, id_number):
    return HttpResponse("Come edit your tutorial person " + id_number)
