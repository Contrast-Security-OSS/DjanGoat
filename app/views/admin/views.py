from django.http import HttpResponse


def admin_index(request):
    return HttpResponse("Admin index")
