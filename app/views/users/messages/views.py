from __future__ import unicode_literals

from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.utils import timezone

from app.decorators import user_is_authenticated
from app.models import User
from app.models import Message
from app.views import utils


@require_http_methods(["GET", "POST"])
@user_is_authenticated
def user_messages(request, user_id):
    current_user = utils.current_user(request)

    if request.method == "GET":
        return render(request, "users/messages/index.html", {
            'current_user': current_user,
            'available_recipients': User.objects.all()
        })
    else:
        Message.objects.create(creator_id=int(request.POST['creator_id']),
                               receiver_id=int(request.POST['receiver_id']),
                               message=request.POST['message'],
                               read=int(request.POST['read']),
                               created_at=str(timezone.now()),
                               updated_at=str(timezone.now()))
        return redirect("/users/" + str(current_user.id) + "/messages")


@require_http_methods(["GET", "DELETE"])
@user_is_authenticated
def user_message(request, user_id, message_id):
    current_user = utils.current_user(request)

    message = Message.objects.get(message_id)
    if request.method == "GET":
        return render(request, "users/messages/show.html", {
            'current_user': current_user,
            'message': message
        })
    else:
        message.delete()
        return redirect("/users/" + str(current_user.id) + "/messages")
