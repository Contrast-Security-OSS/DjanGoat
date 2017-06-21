from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from app.decorators import user_is_authenticated


@require_http_methods(["GET", "POST"])
@user_is_authenticated
def user_benefit_forms(request, user_id):
    return HttpResponse("Benefit forms index" + str(user_id))


@require_http_methods(["GET"])
@user_is_authenticated
def new_user_benefit_form(request, user_id):
    return HttpResponse("New benefit form" + str(user_id))


@require_http_methods(["GET"])
@user_is_authenticated
def edit_user_benefit_form(request, user_id, benefit_form_id):
    return HttpResponse("edit benefit form" + str(user_id) +
                        str(benefit_form_id))


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
@user_is_authenticated
def user_benefit_form(request, user_id, benefit_form_id):
    return HttpResponse("show benefit form" + str(user_id) +
                        str(benefit_form_id))


@require_http_methods(["GET"])
@user_is_authenticated
def download(request):
    return HttpResponse("Download user benefit form")


@require_http_methods(["POST"])
@user_is_authenticated
def upload(request):
    return HttpResponse("Upload user benefit form")
