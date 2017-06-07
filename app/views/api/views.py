from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def api_index(request):
    return HttpResponse('You are at the api index')


@require_http_methods(["GET"])
def api_new(request):
    return HttpResponse('New api')


@require_http_methods(["GET"])
def api_id_edit(request, id_number):
    return HttpResponse('Api Id Edit for user: ' + id_number)


@require_http_methods(["GET", "PUT", "PATCH", "DELETE"])
def api_id(request, id_number):
    return HttpResponse('Api user ' + id_number)
