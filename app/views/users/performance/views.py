from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET', 'POST'])
def user_performance_index(request, user_id):
    return HttpResponse("Usr" + str(user_id) + "performance index")


@require_http_methods(["GET"])
def new_user_performance(request, user_id):
    return HttpResponse("New user performance for user " + str(user_id))


@require_http_methods(["GET"])
def edit_user_performance(request, user_id, performance_id):
    return HttpResponse("Edit performance " + str(performance_id) +
                        " for user " + str(user_id))


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
def user_performance(request, user_id, performance_id):
    return HttpResponse("View performance " + str(performance_id) +
                        " for user " + str(user_id))
