from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def api_index(request):
    if request.GET.__contains__("class"):
        classname = request.GET.__getitem__("class")
        model = eval(classname)
        return JsonResponse(model.objects.all())
    else:
        # what is the equivalent to returning nil (NONE doesn't work bc not dict)
        return HttpResponse('')
    # return JsonResponse({'foo': 'index'})


@require_http_methods(["GET", "PUT", "PATCH", "DELETE"])
def api_id(request, id_number):
    if request.GET.__contains__("class"):
        classname = request.GET.__getitem__("class")
        model = eval(classname)
        return JsonResponse(model.objects.get(id=id_number))
    else:
        return HttpResponse('')
    # return JsonResponse({'id': id_number})
