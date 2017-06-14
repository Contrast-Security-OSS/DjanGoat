from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from app.models import User
from app.models import Analytics


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
def admin_dashboard(request, selected_id):
    return HttpResponse("Admin dashboard with selected_id " + selected_id)


@require_http_methods(["GET"])
def admin_get_user(request, selected_id):
    print("The selected is " + selected_id)
    success = True
    try:
        user = User.objects.get(user_id=int(selected_id))
    except User.DoesNotExist:
        success = False

    return HttpResponse("Admin get user with " + selected_id)


@require_http_methods(["POST"])
def admin_delete_user(request, selected_id):
    success = True
    try:
        user = User.objects.get(user_id=int(selected_id))
        user.delete()
    except User.DoesNotExist:
        success = False

    msg = "success" if success else "failure"
    return JsonResponse({'msg': msg})


@require_http_methods(["PATCH"])
def admin_update_user(request, selected_id):
    success = True
    try:
        user = User.objects.get(user_id=int(selected_id))
        data = request.GET.get('field').dict().copy()
        password = data['password']
        data.pop('password')
        data.pop('password_confirmation')
        user.update(**data)
        if password != '':
            user.password = password
        user.save()
    except User.DoesNotExist:
        success = False

    msg = "success" if success else "failure"
    return JsonResponse({'msg': msg})


@require_http_methods(["GET"])
def admin_get_all_users(request, selected_id):
    users = User.objects.all()
    # render appropriately
    return HttpResponse("Admin number " + selected_id + " wants to get all users")


@require_http_methods(["GET"])
def admin_analytics(request, selected_id):
    if request.GET.get('field', '') == '':
        fields = "*"
    else:
        fields = ', '.join("%s" % (key) for (key, val) in request.GET.dict().iteritems())

    if request.GET.get('ip', '') != '':
        analytics = Analytics.hits_by_ip(request.GET['ip'], fields)
    else:
        analytics = Analytics.objects.all()

    return HttpResponse("Admin analytics " + selected_id)
