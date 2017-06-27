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


# @require_http_methods(["GET"])
# def api_new(request):
#     return JsonResponse({'foo': 'new api'})
#
#
# @require_http_methods(["GET"])
# def api_id_edit(request, id_number):
#     return JsonResponse({'edit': id_number})


@require_http_methods(["GET", "PUT", "PATCH", "DELETE"])
def api_id(request, id_number):
    if request.GET.__contains__("class"):
        classname = request.GET.__getitem__("class")
        model = eval(classname)
        return JsonResponse(model.objects.get(id=id_number))
    else:
        return HttpResponse('')
    # className = request.GET.get("class")
    # if className:
    #     model = eval(className)
    #     return JsonResponse(model.objects.get(id=id_number))
    # return JsonResponse({'id': id_number})
