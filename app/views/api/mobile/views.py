from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers

import json


#Pylint says these are unused by they ARE used during api_index() (specifically, eval(classname))
from app.models import User  # pylint: disable=unused-import

@require_http_methods(["GET"])
def api_index(request):
    if "class" in request.GET:
        classname = request.GET.get("class")
        model = eval(classname)
        serialized = serializers.serialize("json", model.objects.all())
        return JsonResponse(json.loads(serialized), safe=False)
    else:
        return HttpResponse('')


@require_http_methods(["GET"])
def api_id(request, id_number):
    if "class" in request.GET:
        classname = request.GET.get("class")
        model = eval(classname)
        serialized = serializers.serialize("json", [model.objects.get(id=id_number)])
        return JsonResponse(json.loads(serialized), safe=False)
    else:
        return HttpResponse('')

