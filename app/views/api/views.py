from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def api_index(request):
    return JsonResponse({'foo': 'index'})


@require_http_methods(["GET"])
def api_new(request):
    return JsonResponse({'foo': 'new api'})


@require_http_methods(["GET"])
def api_id_edit(request, id_number):
    return JsonResponse({'edit': id_number})


@require_http_methods(["GET", "PUT", "PATCH", "DELETE"])
def api_id(request, id_number):
    return JsonResponse({'id': id_number})
