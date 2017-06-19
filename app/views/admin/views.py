from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from app.models.User.user import User
from app.models.Analytics.analytics import Analytics
from django.shortcuts import render
import pytz
import datetime


@require_http_methods(["GET"])
def admin_dashboard(request, selected_id):
    return render(request, 'admin/dashboard.html')


@require_http_methods(["GET"])
def admin_get_user(request, selected_id):
    success = True
    user = None
    try:
        user = User.objects.get(user_id=int(selected_id))
    except User.DoesNotExist:
        success = False

    if user is None:
        other_is_admin_val = False
    else:
        other_is_admin_val = not user.is_admin

    return render(request, 'admin/modal.html', {'user': user, 'other_admin_val': other_is_admin_val})


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


@require_http_methods(["POST", "PATCH"])
def admin_update_user(request, selected_id):
    success = True
    try:
        user = User.objects.get(user_id=int(selected_id))
        data = request.POST.dict().copy()
        if data:
            password = data['password']
            data.pop('password')
            data.pop('password_confirmation')
            data['updated_at'] = pytz.utc.localize(datetime.datetime.now())
            if password != '':
                user.password = password
                user.save()
        User.objects.filter(user_id=int(selected_id)).update(**data)
    except User.DoesNotExist:
        success = False

    msg = "success" if success else "failure"
    return JsonResponse({'msg': msg})


@require_http_methods(["GET"])
def admin_get_all_users(request, selected_id):
    users = User.objects.all()
    # render appropriately
    users2 = ['dsds', 'f', 'f', 'f']
    return render(request, 'admin/table.html', {'users': users, 'users2': users2})


@require_http_methods(["GET"])
def admin_analytics(request, selected_id):
    data = request.GET.dict().copy()
    show_user_agent = False
    show_ip_address = False
    show_referrer = False

    if 'user_agent' in data or (not data):
        show_user_agent = True

    if 'ip_address' in data or (not data):
        show_ip_address = True

    if 'referrer' in data or (not data):
        show_referrer = True

    if request.GET.get('ip', '') != '':
        analytics = Analytics.hits_by_ip(request.GET['ip'])

    else:
        analytics = Analytics.objects.all()

    return render(request, 'admin/analytics.html', {'analytics': analytics, 'show_user_agent': show_user_agent,
                                                    'show_ip_address': show_ip_address, 'show_referrer': show_referrer})
