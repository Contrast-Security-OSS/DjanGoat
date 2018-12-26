from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, reverse
from wsgiref.util import FileWrapper
from app.decorators import user_is_authenticated
from pygoat.settings import BASE_DIR
from app.models import Benefits
from django.contrib import messages
from app.views import utils
import os


@require_http_methods(["GET", "POST"])
@user_is_authenticated
def user_benefit_forms(request, user_id):  # pylint: disable=unused-argument
    user = utils.current_user(request)
    return render(request, 'users/benefit_forms.html',
                  context={'current_user': user})


@require_http_methods(["GET"])
@user_is_authenticated
def download(request):
    path = BASE_DIR + r"/" + request.GET.get('name', '')
    try:
        wrapper = FileWrapper(file(path))
    except:
        wrapper = None
    response = HttpResponse(wrapper,
                            content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=%s' \
                                      % os.path.basename(path)
    response['Content-Length'] = os.path.getsize(path)
    return response


@require_http_methods(["POST"])
@user_is_authenticated
def upload(request):
    user_id = utils.current_user(request).user_id
    if 'myfile' in request.FILES:
        Benefits.save_data(request.FILES['myfile'], request.POST['backup'])
        messages.success(request, 'File was successfully uploaded!')
    else:
        messages.error(
            request, 'Something went wrong! Are you sure you selected a file?')

    return HttpResponseRedirect(reverse('app:user_benefit_forms',
                                        kwargs={'user_id': user_id}))
