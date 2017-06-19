from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from app.models import User
from django.core import serializers


@require_http_methods(["GET", "POST"])
def api_index(request):
    data = serializers.serialize("json", User.objects.all())
    return HttpResponse(data, content_type='application/json')


@require_http_methods(["GET", "PUT", "PATCH", "DELETE"])
def api(request, id_number):
    try:
        data = serializers.serialize("json", User.objects.filter(user_id=id_number))
        return HttpResponse(data, content_type='application/json')
    except User.DoesNotExist:
        return HttpResponse("null", content_type='application/json')
