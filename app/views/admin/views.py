from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from app.models.User.user import User
from app.models.Analytics.analytics import Analytics
from django.template.loader import get_template
from django.shortcuts import render, redirect
import pytz
import datetime
import django_tables2 as tables
from django_tables2 import RequestConfig
from django_filters.views import FilterView
from django.utils.html import format_html
from django.views.decorators.csrf import csrf_exempt


class ButtonColumn(tables.Column):
    def render(self, value):
        return format_html(
            '<button type="submit" class="btn btn-primary" data-target="#myModal" onclick="openEditModal({})"> Edit </button>',
            value)


class UserTable(tables.Table):
    action = ButtonColumn(verbose_name="action", accessor='user_id', orderable=False)

    class Meta:
        model = User
        template = 'django_tables2/table.html'
        attrs = {'class': 'table table-bordered table-striped table-hover paleblue'}
        exclude = ('password', 'updated_at', 'created_at', 'user_id', 'auth_token')
        sequence = ('id', 'first_name', 'last_name', 'email', 'is_admin', 'action')
        summary = tables.Column(order_by=('id'))


@require_http_methods(["GET", "POST"])
def admin_index(request):
    return HttpResponse("Admin index")


@require_http_methods(["GET"])
def new_admin(request):
    return HttpResponse("Admin New")


@require_http_methods(["GET"])
def edit_admin(request, id):
    return HttpResponse("Admin edit with user " + str(id))


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
def admin(request, id):
    return HttpResponse("Admin with user " + str(id))


@require_http_methods(["GET"])
def admin_dashboard(request, selected_id):
    queryset = User.objects.all()
    table = UserTable(queryset)
    RequestConfig(request, paginate={
        'per_page': 1
    }).configure(table)
    return render(request, 'admin/dashboard.html', {'table': table})


@require_http_methods(["GET"])
def admin_get_user(request, selected_id):
    success = True
    user = None
    try:
        user = User.objects.get(user_id=int(selected_id))
    except User.DoesNotExist:
        success = False

    other_is_admin_val = not user.is_admin
    return render(request, 'admin/modal.html', {'user': user, 'other_admin_val': other_is_admin_val})


@csrf_exempt
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


@csrf_exempt
@require_http_methods(["POST", "PATCH"])
def admin_update_user(request, selected_id):
    success = True
    try:
        user = User.objects.get(user_id=int(selected_id))
        data = request.POST.dict().copy()
        print(request.POST)
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
    if request.GET.get('field', '') == '':
        fields = "*"
    else:
        fields = ', '.join("%s" % (key) for (key, val) in request.GET.dict().iteritems())

    if request.GET.get('ip', '') != '':
        analytics = Analytics.hits_by_ip(request.GET['ip'], fields)
    else:
        analytics = Analytics.objects.all()

    return HttpResponse("Admin analytics " + str(selected_id))
