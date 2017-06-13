from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def admin_index(request):
    return HttpResponse("Admin index")


@require_http_methods(["GET"])
def new_admin(request):
    return HttpResponse("Admin New")


@require_http_methods(["GET"])
def edit_admin(request, id):
    return HttpResponse("Admin edit with user " + id)


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
def admin(request, id):
    return HttpResponse("Admin with user " + id)


@require_http_methods(["GET"])
def admin_dashboard(request, admin_id):
    return HttpResponse("Admin dashboard with admin_id " + admin_id)


@require_http_methods(["GET"])
def admin_get_user(request, admin_id):
    return HttpResponse("Admin get user with " + admin_id)


@require_http_methods(["POST"])
def admin_delete_user(request, admin_id):
    return HttpResponse("Admin delete with number " + admin_id)


@require_http_methods(["PATCH"])
def admin_update_user(request, admin_id):
    return HttpResponse("Admin update user with number " + admin_id)


@require_http_methods(["GET"])
def admin_get_all_users(request, admin_id):
    return HttpResponse("Admin number " + admin_id + " wants to get all users")


@require_http_methods(["GET"])
def admin_analytics(request, admin_id):
    return HttpResponse("Admin analytics " + admin_id)
