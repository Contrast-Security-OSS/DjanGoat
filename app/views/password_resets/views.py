from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
def forgot_password(request):
    return HttpResponse('You forgot your password! PANICCCCCC')


@require_http_methods(["GET"])
def confirm_token(request):
    return HttpResponse('Confirm your token please!')


@require_http_methods(["POST"])
def reset_password(request):
    return HttpResponse('Reset your password')



