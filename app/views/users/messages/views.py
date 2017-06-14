from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.template.loader import get_template


@require_http_methods(["GET", "POST"])
def user_messages(request, user_id):
    return HttpResponse(str(user_id) + "Messages Index!")


@require_http_methods(["GET"])
def new_user_message(request, user_id):
    return HttpResponse(str(user_id) + "New Message!")


@require_http_methods(["GET"])
def edit_user_message(request, user_id, message_id):
    return HttpResponse("edit user message" + str(user_id) + str(message_id))


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
def user_message(request, user_id, message_id):
    return HttpResponse("show user message" + str(user_id) + str(message_id))
