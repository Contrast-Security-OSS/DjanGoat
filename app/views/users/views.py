from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.urls import reverse
from app.models import User
from django.contrib import messages
from django.utils import timezone


@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == "POST":
        form = request.POST
        if not form:
            return HttpResponse("Users index")
        email = form["email"]
        first_name = form["first_name"]
        last_name = form["last_name"]
        password = form["password"]
        confirm = form["confirm"]
        err_list = []
        if password != confirm:
            err_list.append("Password and Confirm Password does not match")
        if User.objects.filter(email=email):
            err_list.append("Email has already been taken")
        err_msg = " and ".join(err_list)
        if len(err_msg) > 0:
            messages.add_message(request, messages.INFO, err_msg)
            return redirect("/signup/", permanent=False)
        else:
            try:
                User.objects.create(email=email,
                                    password=password, is_admin=False,
                                    first_name=first_name, last_name=last_name,
                                    created_at=timezone.now(),
                                    updated_at=timezone.now(),
                                    )
                return redirect("/dashboard/home", permanent=False)
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
def edit_user(request, user_id):
    return HttpResponse("Edit user " + str(user_id))


@require_http_methods(["GET"])
def account_settings(request, user_id):
    return HttpResponse("Account settings for user #" + str(user_id))


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
def user_view(request, user_id):
    return HttpResponse("User " + str(user_id) + " " + str(request.method))
