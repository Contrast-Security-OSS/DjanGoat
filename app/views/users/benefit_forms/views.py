from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def user_benefit_forms(request, user_id):
    return HttpResponse("Benefit forms for user " + str(user_id))


@require_http_methods(["GET"])
def new_user_benefit_form(request, user_id):
    return HttpResponse("New benefit forms for user " + str(user_id))


@require_http_methods(["GET"])
def edit_user_benefit_form(request, user_id, benefit_form_id):
    return HttpResponse("Edit benefit form " + str(benefit_form_id) + " for user " + str(user_id))


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
def user_benefit_form(request, user_id, benefit_form_id):
    return HttpResponse("View benefit form " + str(benefit_form_id) + " for user " + str(user_id))


@require_http_methods(["GET"])
def download(request):
    return HttpResponse("Donwload user benefit form")


@require_http_methods(["POST"])
def upload(request):
    return HttpResponse("Upload user benefit form")
