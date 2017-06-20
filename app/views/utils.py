from app.models import User


def current_user(request):
    return User.authenticate(request.COOKIES['auth_token'])
