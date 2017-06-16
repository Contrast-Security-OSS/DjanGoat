from app.models import User
from django.http import HttpResponse


def user_is_authenticated(function):

    def wrap(request, *args, **kwargs):
        if 'auth_token' in request.COOKIES:
            try:
                user = User.objects.get(auth_token=request.COOKIES['auth_token'])
                return function(request, *args, **kwargs)
            except User.DoesNotExist:
                return HttpResponse("Sorry, but you are no longer logged in to your session. Please log in again")
        else:
            return HttpResponse("Sorry, but you are not logged in. Please log in again")

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
