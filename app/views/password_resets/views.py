from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.urls import reverse
from app.models import User
from django.core.mail import send_mail
from Crypto.Hash import MD5


@require_http_methods(["POST"])
def forgot_password(request):
    if len(User.objects.filter(email=request.POST['email'])) > 0:
        user = User.objects.filter(email=request.POST['email']).first()
        messages.success(request,
                         'An email was sent to your email to reset your password!')
        password_reset_mailer(request, user)
    else:
        messages.error(request, 'We do not have the email in our system')

    return HttpResponseRedirect('/login')


def password_reset_mailer(request, user):
    token = generate_token(user.user_id, user.email)
    message = 'Use this link: ' + 'localhost:8000' + reverse(
        'app:password_resets') + '?token=' + token
    send_mail(
        'Reset your Metacorp Password',
        message,
        'noreply@djanGoat.dev',
        ['vinai.rachakonda@contrastsecurity.com'],
        fail_silently=False,
    )


def generate_token(id, email):
    h = MD5.new()
    h.update(email)
    return str(id) + '-' + str(h.hexdigest())


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
    if 'token' in request.GET.values() and is_valid_token(request.GET('token')):
        return HttpResponse('Ay you can rest')
    else:
        print(request.GET['token'])
        return HttpResponse('Bad token!')


@require_http_methods(["POST"])
def reset_password(request):
    return HttpResponse('Reset your password')


def is_valid_token(token):
    split = token.split('-')
    if split[0] and split[1]:
        user = User.objects.filter(user_id=split[0]).first()
        email = user.email
        h = MD5.new()
        h.update(email)
        return split[1] == h.hexdigest()
    else:
        return False
