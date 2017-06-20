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
    # fake_user = User.objects.create
    #     user_id=6,
    #     email='catdog@catdog.com', password='dogcat',
    #     is_admin='False', first_name='cat',
    #     last_name='dog', created_at='2017-01-01 12:12',
    #     updated_at='2017-01-01 12:12'
    # )
    #
    # retirement_info = Retirement.objects.create(
    #     total=5000,
    #     employer_contrib=2342,
    #     employee_contrib=2555,
    #     created_at=pytz.utc.localize(datetime.datetime(2017, 1, 1, 0, 0)),
    #     updated_at=pytz.utc.localize(datetime.datetime(2017, 1, 1, 0, 0)),
    #     user_id = fake_user.user_id
    # )

    current_user = utils.current_user(request)
    retirement_info = current_user.retirement
    t = get_template('users/retirement/index.html')
    html = t.render({'retirement': retirement_info})
    return HttpResponse(html)

