from app.models import User
from django.http import HttpResponseRedirect


def user_is_authenticated(function):

    def wrap(request, *args, **kwargs):
        if 'auth_token' in request.COOKIES:
            try:
                User.objects.get(auth_token=request.COOKIES['auth_token'])
                return function(request, *args, **kwargs)
            except User.DoesNotExist:
                return HttpResponseRedirect('/login')
        else:
            return HttpResponseRedirect('/login')

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
