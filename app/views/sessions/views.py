from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def login(request):
    return HttpResponse('You logged in!')


@require_http_methods(["GET"])
def logout(request):
    return HttpResponse('You logged out')


@require_http_methods(["GET", "POST"])
def sessions_index(request):
    return HttpResponse('You are at the sessions index')


@require_http_methods(["GET"])
def new_sessions(request):
    return HttpResponse('You created a new session')


@require_http_methods(["GET"])
def edit_session(request, id_number):
    return HttpResponse('User ' + id_number + ' edited a session')


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
def session_id(request, id_number):
    return HttpResponse(id_number + ' is at a session')