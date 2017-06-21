from app.models import User


def current_user(request):
    return User.authenticate_by_token(request.COOKIES['auth_token'])
