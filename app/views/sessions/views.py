from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods

from app.models.User.user import User


@require_http_methods(["GET"])
def login(request):
    return HttpResponse('You logged in!')


@require_http_methods(["GET"])
def logout(request):
    return HttpResponse('You logged out')


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

        try:
            response = HttpResponseRedirect(path)
            user = User.authenticate(email, password)
            response.set_cookie("auth_token", user.auth_token)
            return response
        except User.DoesNotExist:
            return HttpResponse("Email or password incorrect!")
        except Exception as error:
            if u'Incorrect Password' in error.message:
                return HttpResponse("Email or password incorrect!")
            else:
                raise error

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