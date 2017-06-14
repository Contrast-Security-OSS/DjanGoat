from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.template.loader import get_template


@require_http_methods(["GET", "POST"])
def user_benefit_forms(request, user_id):
    t = get_template('users/benefit_forms/index.html')
    c = {'user_id': user_id}
    return HttpResponse(t.render(c, request))


@require_http_methods(["GET"])
def new_user_benefit_form(request, user_id):
    t = get_template('users/benefit_forms/new.html')
    c = {'user_id': user_id}
    return HttpResponse(t.render(c, request))


@require_http_methods(["GET"])
def edit_user_benefit_form(request, user_id, benefit_form_id):
    t = get_template('users/benefit_forms/edit.html')
    c = {'user_id': user_id, 'benefit_form_id': benefit_form_id}
    return HttpResponse(t.render(c, request))


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
def user_benefit_form(request, user_id, benefit_form_id):
    t = get_template('users/benefit_forms/show.html')
    c = {'user_id': user_id, 'benefit_form_id': benefit_form_id}
    return HttpResponse(t.render(c, request))


@require_http_methods(["GET"])
def download(request):
    return HttpResponse("Download user benefit form")


@require_http_methods(["POST"])
def upload(request):
    return HttpResponse("Upload user benefit form")
