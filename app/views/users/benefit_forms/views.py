from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, reverse
from wsgiref.util import FileWrapper
from app.decorators import user_is_authenticated
from pygoat.settings import BASE_DIR
from app.models import Benefits, User
from django.contrib import messages
from app.views import utils
import os


@require_http_methods(["GET", "POST"])
@user_is_authenticated
def user_benefit_forms(request, user_id):
    user = utils.current_user(request)
    return render(request, 'users/benefit_forms.html', context={'current_user': user})


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
    path = BASE_DIR + r"/" + request.GET.get('name')
    wrapper = FileWrapper(file(path))
    response = HttpResponse(wrapper, content_type='application/pdf')  # hard coded for now
    response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(path)
    response['Content-Length'] = os.path.getsize(path)
    return response


@require_http_methods(["POST"])
@user_is_authenticated
def upload(request):
    id = utils.current_user(request).user_id
    if 'myfile' in request.FILES:
        Benefits.save_data(request.FILES['myfile'])
        messages.success(request, 'File was successfully uploaded!')
    else:
        messages.error(request, 'Something went wrong! Are you sure you selected a file?')

    return HttpResponseRedirect(reverse('app:user_benefit_forms', kwargs={'user_id': id}))
