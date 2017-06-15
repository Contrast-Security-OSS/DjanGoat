from django.core.exceptions import PermissionDenied
from app.models import User


def user_is_authenticated(function):
    def wrap(request, *args, **kwargs):
        try:
            user = User.objects.get(auth_token=request.cookies['auth_token'])

            if user is not None:
                return function(request, *args, **kwargs)
            else:
                raise PermissionDenied
        except AttributeError:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
