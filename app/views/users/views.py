from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def index(request):
    return HttpResponse("Users index")


@require_http_methods(["GET"])
def new_user(request):
    return HttpResponse("New user")


@require_http_methods(["GET"])
def signup(request):
    return HttpResponse("Signup user")


@require_http_methods(["GET"])
def edit_user(request, user_id):
    return HttpResponse("Edit user " + str(user_id))


@require_http_methods(["GET"])
def account_settings(request, user_id):
    return HttpResponse("Account settings for user #" + str(user_id))


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
def user_view(request, user_id):
    return HttpResponse("User " + str(user_id) + " " + str(request.method))
