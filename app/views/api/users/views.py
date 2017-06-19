from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def api_index(request):
    return JsonResponse({'all': 'users'})


@require_http_methods(["GET", "PUT", "PATCH", "DELETE"])
def api(request, id_number):
    return JsonResponse({'id': id_number})
