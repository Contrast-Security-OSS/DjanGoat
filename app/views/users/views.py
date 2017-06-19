from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from app.decorators import user_is_authenticated


@require_http_methods(["GET"])
def new_user(request):
    return HttpResponse("New user")


@require_http_methods(["GET"])
def signup(request):
    return HttpResponse("Signup user")


@require_http_methods(["GET"])
@user_is_authenticated
def edit_user(request, user_id):
    return HttpResponse("Edit user " + str(user_id))


@require_http_methods(["GET"])
@user_is_authenticated
def account_settings(request, user_id):
    return HttpResponse("Account settings for user #" + str(user_id))


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
@user_is_authenticated
def user_view(request, user_id):
    return HttpResponse("User " + str(user_id) + " " + str(request.method))
