from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.template.loader import get_template


@require_http_methods(["GET", "POST"])
def user_messages(request, user_id):
    t = get_template('users/messages/index.html')
    c = {'user_id': user_id}
    return HttpResponse(t.render(c, request))


@require_http_methods(["GET"])
def new_user_message(request, user_id):
    t = get_template('users/messages/new.html')
    c = {'user_id': user_id}
    return HttpResponse(t.render(c, request))


@require_http_methods(["GET"])
def edit_user_message(request, user_id, message_id):
    t = get_template('users/messages/edit.html')
    c = {'user_id': user_id, 'message_id': message_id}
    return HttpResponse(t.render(c, request))


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
def user_message(request, user_id, message_id):
    t = get_template('users/messages/show.html')
    c = {'user_id': user_id, 'message_id': message_id}
    return HttpResponse(t.render(c, request))
