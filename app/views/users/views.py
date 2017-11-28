from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from app.decorators import user_is_authenticated
from django.shortcuts import render, redirect
from app.models import User
from django.contrib import messages
from django.utils import timezone
from app.views import utils


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
        return HttpResponseRedirect("/signup/")

    else:
        return HttpResponse("Users index")


@require_http_methods(["GET"])
def signup(request):
    return render(request, "users/signup.html")


@require_http_methods(["GET"])
@user_is_authenticated
def account_settings(request, user_id):
    user = utils.current_user(request)
    if not user:
        return HttpResponse("User " + str(user_id) + " NOT FOUND")
    else:
        context = user.__dict__
        context.update({'current_user': user})
        return render(request, "users/account_settings.html",
                      context=context)


@require_http_methods(["GET", "POST", "PUT", "DELETE"])
@user_is_authenticated
def user_view(request, user_id):
    if request.method == "POST":
        form = request.POST
        if not form:
            return HttpResponse("User " + str(user_id) + "POST")
        user_id_form = form['user_id']
        table_name = User.objects.model._meta.db_table
        # The order by is_admin='0' moves admin to the first in list
        # which allows sql injection
        users = User.objects.raw(
            "SELECT * FROM %s WHERE user_id='%s' ORDER BY is_admin='0'"
            % (table_name, user_id_form))
        try:
            user = users[0]
        except:
            return HttpResponse("User " + str(user_id_form) + " NOT FOUND")
        update = dict()
        err_msg = User.validate_update_form(form, user, update)
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
