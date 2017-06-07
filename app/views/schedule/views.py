from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def schedule_index(request):
    return HttpResponse("Schedule index")

@require_http_methods(["GET"])
def get_pto_schedule_schedule_index(request):
    return HttpResponse("PTO schedule index")

@require_http_methods(["GET"])
def new_schedule(request):
    return HttpResponse("New shcedule")

@require_http_methods(["GET"])
def edit_schedule(request, schedule_id):
    return HttpResponse("Edit schedule" + str(schedule_id))

@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
def schedule(request, schedule_id):
    return HttpResponse("View schedule " + str(schedule_id) )
