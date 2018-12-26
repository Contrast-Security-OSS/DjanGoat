from __future__ import unicode_literals

from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from app.models import User
from Crypto.Hash import MD5
import pickle
import base64


@require_http_methods(["POST"])
def forgot_password(request):
    qset = User.objects.filter(email=request.POST.get('email', ''))
    if len(qset) > 0:
        user = qset.first()
        messages.success(request, 'An email was sent to reset your password!')
        password_reset_mailer(request, user)
    else:
        try:
            messages.error(request, 'We do not have the email in our system')
        except:
            pass

    return redirect('/login')


def password_reset_mailer(request, user):  # pylint: disable=unused-argument
    token = generate_token(user.user_id, user.email)
    message = 'Use this link: ' + 'localhost:8000' + reverse(
        'app:password_resets') + '?token=' + token
    send_mail(
        'Reset your Metacorp Password',
        message,
        'noreply@djanGoat.dev',
        ['vinai.rachakonda@contrastsecurity.com'],
        fail_silently=False
    )


def generate_token(user_id, email):
    h = MD5.new()
    h.update(email)
    return str(user_id) + '-' + str(h.hexdigest())


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
    if request.GET.get('token', '') != '' and is_valid_token(
            request.GET['token']):
        messages.success(request, 'Please create a new password.')
        user_id = request.GET['token'].split('-')[0]
        user = User.objects.filter(user_id=user_id).first()
        encoded = base64.b64encode(pickle.dumps(user))

        return render(request, 'password_reset/reset.html',
                      context={'user': encoded})
    else:
        try:
            messages.error(request, 'Bad token')
        except:
            pass

        return HttpResponseRedirect(reverse('app:login'))


@require_http_methods(["POST"])
def reset_password(request):
    if request.POST.get('user', '') != '':
        encoded_user = request.POST['user']
        user = pickle.loads(base64.b64decode(encoded_user))
        user.password = request.POST['password']
        user.save()
        messages.success(request, 'Your password has been updated')
    else:
        try:
            messages.error(request, 'Password did not reset')
        except:
            pass

    return redirect('/login')


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
