from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def user_work_info_index(request, user_id):
    return HttpResponse("Work info index for user: " + str(user_id))


@require_http_methods(["GET"])
def new_user_work_info(request, user_id):
    return HttpResponse("New work info for user " + str(user_id))


@require_http_methods(["GET"])
def edit_user_work_info(request, user_id, work_info_id):
    return HttpResponse("Edit work info with id " +
                        str(work_info_id) + " for user " + str(user_id))


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
def user_work_info(request, user_id, work_info_id):
    return HttpResponse("View work info " +
                        str(work_info_id) + " for user " + str(user_id))