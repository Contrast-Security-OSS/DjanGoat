from __future__ import unicode_literals

from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.utils import timezone

from app.decorators import user_is_authenticated
from app.models import User, Message
from app.views import utils


@require_http_methods(["GET", "POST"])
@user_is_authenticated
def user_messages(request, user_id):  # pylint: disable=unused-argument
    current_user = utils.current_user(request)

    if request.method == "GET":
        return render(request, "users/messages/index.html", {
            'current_user': current_user,
            'available_recipients': User.objects.all()
        })
    else:
        try:
            cid = int(request.POST['creator_id'])
            creator = User.objects.get(user_id=cid)
            rid = int(request.POST['receiver_id'])
            receiver = User.objects.get(user_id=rid)
            msg = request.POST['message']
            red = int(request.POST['read'])
            now = timezone.now()
            Message.objects.create(creator=creator, receiver=receiver,
                                   message=msg, read=red,
                                   created_at=now, updated_at=now)
            return redirect("/users/" + str(current_user.id) + "/messages")
        except Exception as e:
            messages.add_message(request, messages.INFO, str(e))
            return render(request, "users/messages/index.html", {
                'current_user': current_user,
                'available_receipients': User.objects.all()
            })


# W0613 = unused-argument
@require_http_methods(["GET", "DELETE"])
@user_is_authenticated
def user_message(request, user_id, message_id):  # pylint: disable=W0613
    current_user = utils.current_user(request)
    try:
        message = Message.objects.get(pk=message_id)
        if request.method == "GET":
            return render(request, "users/messages/show.html", {
                'current_user': current_user,
                'message': message
            })
        else:
            message.delete()
            return HttpResponse("Success!")
    except Exception:
        return redirect("/users/" + str(current_user.id) + "/messages")
