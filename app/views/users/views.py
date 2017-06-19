from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.urls import reverse
from app.models import User
from django.contrib import messages
from django.utils import timezone
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
def edit_user(request, user_id):
    return HttpResponse("Edit user " + str(user_id))


@require_http_methods(["GET"])
def account_settings(request, user_id):
    user = User.objects.filter(user_id=user_id).first()
    if not user:
        return HttpResponse("User " + str(user_id) + " NOT FOUND")
    else:
        return render(request, "users/account_settings.html",
                      context=user.__dict__)


@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def user_view(request, user_id):
    if request.method == "POST":
        form = request.POST
        if not form:
            return HttpResponse("User " + str(user_id) + "POST")
        table_name = User.objects.model._meta.db_table
        users = User.objects.raw("SELECT * FROM %s WHERE user_id='%s'"
                                 % (table_name, user_id))
        try:
            user = users[0]
        except:
            return HttpResponse("User " + str(user_id) + " NOT FOUND")
        update = dict()
        err_msg = User.validate_update_form(form, update)
        if len(err_msg) > 0:
            messages.add_message(request, messages.INFO, err_msg)
        else:
            try:
                # skip hash_password if password not updated
                if "password" not in update:
                    User.objects.filter(pk=user.pk).update(**update)
                else:
                    user.__dict__.update(update)
                    user.save()
                messages.add_message(request, messages.INFO,
                                     "Successfully Updated")
            except Exception as e:
                messages.add_message(request, messages.INFO, str(e))
        return redirect("/users/%s/account_settings" % user_id,
                        permanent=False)

    else:
        return HttpResponse("User " + str(user_id) + " " + str(request.method))
