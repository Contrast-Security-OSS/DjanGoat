from app.models import User
from django.http import HttpResponseForbidden
from django.http import HttpResponse


def user_is_authenticated(function):
    def wrap(request, *args, **kwargs):
        try:
            user = User.objects.get(auth_token=request.cookies['auth_token'])

            if user is not None:
                return function(request, *args, **kwargs)
            else:
                return HttpResponse("Sorry, but you are no longer logged in to your session. Please log in again")
        except AttributeError:
            return HttpResponse("Sorry, but you are not logged in. Please log in again")

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
