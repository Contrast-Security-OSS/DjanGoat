from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from app.decorators import user_is_authenticated


@require_http_methods(["GET", "POST"])
@user_is_authenticated
def user_retirement_index(request, user_id):
    return HttpResponse("User " + str(user_id) + " retirement index")


@require_http_methods(["GET"])
@user_is_authenticated
def new_user_retirement(request, user_id):
    return HttpResponse("New user retirement for user " + str(user_id))


@require_http_methods(["GET"])
@user_is_authenticated
def edit_user_retirement(request, user_id, retirement_id):
    return HttpResponse("Edit retirement " + str(retirement_id) +
                        " for user " + str(user_id))


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
@user_is_authenticated
def user_retirement(request, user_id, retirement_id):
    return HttpResponse("View retirement " + str(retirement_id) +
                        " for user " + str(user_id))
