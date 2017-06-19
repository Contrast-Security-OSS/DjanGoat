from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from app.decorators import user_is_authenticated
from django.shortcuts import render, redirect
from django.urls import reverse
from app.models import User
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import login
from django.conf import settings


@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == "POST":
        form = request.POST
        if not form:
            return HttpResponse("Users index")
        err_msg = User.validate_signup_form(form)
        if len(err_msg) > 0:
            messages.add_message(request, messages.INFO, err_msg)
        else:
            try:
                user = User.objects.create(email=form["email"],
                                           password=form["password"],
                                           is_admin=False,
                                           first_name=form["first_name"],
                                           last_name=form["last_name"],
                                           created_at=timezone.now(),
                                           updated_at=timezone.now(),
                                           )
                user.build_benefits_data()
                auth = User.authenticate(form["email"], form["password"])
                response = redirect("/dashboard/home", permanent=False)
                response.set_cookie('auth_token', auth.auth_token)
                return response
            except Exception as e:
                messages.add_message(request, messages.INFO, str(e))
        return redirect("/signup/", permanent=False)

    else:
        return HttpResponse("Users index")


@require_http_methods(["GET"])
def new_user(request):
    return HttpResponse("New user")


@require_http_methods(["GET"])
def signup(request):
    return render(request, "users/signup.html")


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
