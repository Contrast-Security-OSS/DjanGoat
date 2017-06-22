from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.template.loader import get_template
from app.models import Retirement
from app.models import User
import datetime
import pytz
from app.views import utils
from app.decorators import user_is_authenticated


@require_http_methods(["GET", "POST"])
@user_is_authenticated
def user_retirement_index(request, user_id):
    current_user = utils.current_user(request)
    retirement_info = current_user.retirements.first()
    t = get_template('users/retirement/index.html')
    html = t.render({'retirement': retirement_info,
                     'current_user': current_user})
    return HttpResponse(html)
