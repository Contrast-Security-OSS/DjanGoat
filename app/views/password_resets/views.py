from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from app.models import User
from django.core.mail import send_mail


@require_http_methods(["POST"])
def forgot_password(request):
    if len(User.objects.filter(email=request.POST['email'])) > 0:
        user = User.objects.filter(email=request.POST['email']).first()
        messages.success(request,
                         'An email was sent to your email to reset your password!')
    else:
        messages.error(request, 'We do not have the email in our system')

    return HttpResponseRedirect('/login')


def password_reset_mailer(request, user):
    return "dsd"


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
