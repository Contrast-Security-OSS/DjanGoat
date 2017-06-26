from __future__ import unicode_literals

from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from app.decorators import user_is_authenticated
from app.models import User


@require_http_methods(["GET", "POST"])
@user_is_authenticated
def user_work_info_index(request, user_id):
    user = User.objects.get(id=user_id)
    work_info = user.work_info.first()
    context = {'current_user': user,
               'work_info': work_info}
    return render(request, "users/work_info/index.html", context=context)
