from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def index(request, user_id):
    return HttpResponse("Paid time off index for user " + user_id)


@require_http_methods(["GET"])
def new(request, user_id):
    return HttpResponse("You made a new pto for user " + user_id)


@require_http_methods(["GET"])
def edit(request, user_id, id):
    return HttpResponse("Edit PTO for user " + user_id + " with id " + id)


@require_http_methods(["GET", "PATCH", "DELETE", "PUT"])
def pto_id(request, user_id, id):
    return HttpResponse("Show, update, or destroy PTO for user " + user_id +
                        " with id " + id)
