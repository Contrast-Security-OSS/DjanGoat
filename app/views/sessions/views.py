from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, render
from django.contrib import messages
from app.models.User.user import User


@require_http_methods(["GET"])
def login(request):
    return render(request, "sessions/login.html")


@require_http_methods(["GET"])
def logout(request):
    response = redirect("/login")
    response.delete_cookie('auth_token')
    return response


def validate_login_form(form):
    err_list = []
    if 'email' not in form or form['email'] is None:
        err_list.append("Error: no email inputted")
    if 'password' not in form or form['password']is None:
        err_list.append("Error: no password inputted")
    err_msg = " and ".join(err_list)
    return err_msg


@require_http_methods(["GET", "POST"])
def sessions_index(request, email=None, password=None, path='/dashboard/home'):

    if request.method == "POST":

        form = request.POST
        if not form:
            return HttpResponse("POST with no form")
        err_msg = validate_login_form(form)

        if len(err_msg) > 0:
            messages.add_message(request, messages.INFO, err_msg)
        else:
            try:
                if 'path' in form:
                    path = form['path']
                else:
                    path = '/dashboard/home'
                response = HttpResponseRedirect(path)
                user = User.authenticate(form['email'], form['password'])
                response.set_cookie("auth_token", user.auth_token)
                return response
            except User.DoesNotExist:
                messages.add_message(request, messages.INFO,
                                     "Email or password incorrect!")
            except Exception as error:
                if u'Incorrect Password' in error.message:
                    messages.add_message(request, messages.INFO,
                                         "Email or password incorrect!")
                else:
                    messages.add_message(request, messages.INFO, error)
        return HttpResponseRedirect("/login/")

    else:
        return HttpResponse("Sessions Index")


@require_http_methods(["GET"])
def new_sessions(request):
    return HttpResponse("You're creating a new session!")


@require_http_methods(["GET"])
def edit_session(request, id_number):
    return HttpResponse('User ' + str(id_number) + ' edited a session')


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
def session_id(request, id_number):
    return HttpResponse(str(id_number) + ' is at a session')