from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from app.models import User


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
    user = User.objects.get(user_id=user_id)
    return render(request, "users/account_settings.html",
                  context=user.__dict__)


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
def user_view(request, user_id):
    return HttpResponse("User " + str(user_id) + " " + str(request.method))
