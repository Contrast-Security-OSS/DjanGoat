

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
def forgot_password(request):
    return HttpResponse('You forgot your password! PANICCCCCC')


# Handler that depending on request type delegated to confirm_token
# or reset_password
@require_http_methods(["GET", "POST"])
def reset_password_handler(request):
    if request.method == 'GET':
        return confirm_token(request)
    else:
        return reset_password(request)


@require_http_methods(["GET"])
def confirm_token(request):
    return HttpResponse('Confirm your token please!')


@require_http_methods(["POST"])
def reset_password(request):
    return HttpResponse('Reset your password')
