from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from app.decorators import user_is_authenticated


@require_http_methods(["GET", "POST"])
@user_is_authenticated
def index(request, user_id):
    return HttpResponse("Paid time off index for user " + str(user_id))


@require_http_methods(["GET"])
@user_is_authenticated
def new(request, user_id):
    return HttpResponse("You made a new pto for user " + str(user_id))


@require_http_methods(["GET"])
@user_is_authenticated
def edit(request, user_id, id):
    return HttpResponse("Edit PTO for user " + str(user_id) + " with id " +
                        str(id))


@require_http_methods(["GET", "PATCH", "DELETE", "PUT"])
@user_is_authenticated
def pto_id(request, user_id, id):
    return HttpResponse("Show, update, or destroy PTO for user " +
                        str(user_id) + " with id " + str(id))
