from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from app.views import utils
from app.decorators import user_is_authenticated


@require_http_methods(["GET", "POST"])
@user_is_authenticated
def user_retirement_index(request, user_id):  # pylint: disable=unused-argument
    current_user = utils.current_user(request)
    retirement_info = current_user.retirements.first()
    context = {'retirement': retirement_info,
               'current_user': current_user}
    return render(request, 'users/retirement/index.html', context=context)
