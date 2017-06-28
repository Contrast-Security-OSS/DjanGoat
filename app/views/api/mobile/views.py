import json

from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def api_index(request):
    if request.GET.__contains__("class"):
        classname = request.GET.get("class")
        model = eval(classname)
        serialized = serializers.serialize("json", model.objects.all())
        return JsonResponse(json.loads(serialized), safe=False)
    else:
        return HttpResponse('')


@require_http_methods(["GET"])
def api_id(request, id_number):
    if request.GET.__contains__("class"):
        classname = request.GET.get("class")
        model = eval(classname)
        serialized = serializers.serialize("json", [model.objects.get(id=id_number)])
        return JsonResponse(json.loads(serialized), safe=False)
    else:
        return HttpResponse('')
