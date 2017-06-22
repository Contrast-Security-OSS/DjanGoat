from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, render
from django.contrib import messages
from app.models.User.user import User
from django.contrib.messages import get_messages


@require_http_methods(["GET"])
def login(request):
    return render(request, "sessions/login.html")


@require_http_methods(["GET"])
def logout(request):
    response = redirect("/login")
    response.delete_cookie('auth_token')
    return response


@require_http_methods(["GET", "POST"])
def sessions_index(request, email=None, password=None, path='/dashboard/home'):

    if request.method == "POST":

        # Set path variable
        if 'path' in request.POST:
            path = request.POST['path']

        # Set email variable
        if 'email' in request.POST:
            email = request.POST['email']
        elif email is None:
            return HttpResponse("Error: no email inputted")

        # Set password variable
        if 'password' in request.POST:
            password = request.POST['password']
        elif password is None:
            return HttpResponse("Error: no password inputted")

        message = ""
        try:
            response = HttpResponseRedirect(path)
            user = User.authenticate(email, password)
            response.set_cookie("auth_token", user.auth_token)
            return response
        except User.DoesNotExist:
            message = "Email or password incorrect!"
        except Exception as error:
            if u'Incorrect Password' in error.message:
                message = "Email or password incorrect!"
            else:
                message = str(error)
        messages.add_message(request, messages.INFO, message)

        response = HttpResponseRedirect("/login/")
        response['message'] = message
        return response

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