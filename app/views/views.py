from __future__ import unicode_literals
from app.models import User


def current_user(request):
    auth_token = request.COOKIES['auth_token']
    return User.authenticate(auth_token)

