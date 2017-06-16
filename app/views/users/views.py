from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from app.models import User
from django.db.models import signals
from app.signals import create_user_values
from django.contrib import messages


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
        user = User.objects.raw("SELECT * FROM %s WHERE user_id='%s'"
                                % (table_name, ip))
        if not user:
            return HttpResponse("User " + str(user_id) + " NOT FOUND")
        email = form["email"]
        first_name = form["first_name"]
        last_name = form["last_name"]
        password = form["password"]
        confirm = form["confirm"]
        err_list = []
        update = dict()
        if password != confirm:
            err_list.append("Password and Confirm Password does not match")
        elif len(password) != 0:
            if len(password) < 6:
                err_list.append("Password minimum 6 characters")
            elif len(password) > 40:
                err_list.append("Password maximum 40 characters")
            else:
                update["password"] = password
        if len(email) > 0:
            if User.objects.filter(email=email):
                err_list.append("Email has already been taken")
            else:
                update["email"] = email
        if len(first_name) > 0:
            update["first_name"] = first_name
        if len(last_name) > 0:
            update["last_name"] = last_name
        err_msg = " and ".join(err_list)
        if len(err_msg) > 0:
            messages.add_message(request, messages.INFO, err_msg)
        else:
            if signals.pre_save.disconnect(create_user_values, sender=User):
                try:
                    user.__dict__.update(update)
                    user.save()
                    success_message = "Successfully Updated"
                    for col in update:
                        success_message += " " + str(col)
                    messages.add_message(request, messages.INFO,
                                         success_message)
                except Exception as e:
                    messages.add_message(request, messages.INFO, str(e))
                finally:
                    signals.pre_save.connect(create_user_values, sender=User)
            else:
                # unable to disconnect signal
                messages.add_message(request, messages.INFO, "Update Failed")
        return redirect("/users/%s/account_settings" % user_id,
                        permanent=False)
    return HttpResponse("User " + str(user_id) + " " + str(request.method))
