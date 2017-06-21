from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect

from app.decorators import user_is_authenticated
from app.models import User
from app.models import Message


@require_http_methods(["GET", "POST"])
# @user_is_authenticated
def user_messages(request, user_id):
    return render(request, "users/messages/index.html", { 'current_user': None })


@require_http_methods(["GET", "DELETE"])
# @user_is_authenticated
def user_message(request, user_id, message_id):
    return render(request, "users/messages/show.html", { 'current_user': None })
