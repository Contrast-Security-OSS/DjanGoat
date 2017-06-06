from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def user_retirement_index(request, user_id):
    return HttpResponse("User " + str(user_id) + " retirement index")

# @require_http_methods(["GET"])
# def new_user_message(request, user_id):
#     return HttpResponse("New message for user " + str(user_id))
#
# @require_http_methods(["GET"])
# def edit_user_message(request, user_id, message_id):
#     return HttpResponse("Edit message " + str(message_id) + " for user " + str(user_id))
#
# @require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
# def user_message(request, user_id, message_id):
#     return HttpResponse("View message " + str(message_id) + " for user " + str(user_id))
