from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.template.loader import get_template
from app.models import Retirement
from app.models import User
import datetime
import pytz


@require_http_methods(["GET", "POST"])
def user_retirement_index(request, user_id):
    fake_user = User.objects.create(
        user_id=6,
        email='catdog@catdog.com', password='dogcat',
        is_admin='False', first_name='cat',
        last_name='dog', created_at='2017-01-01 12:12',
        updated_at='2017-01-01 12:12'
    )

    retirement_info = Retirement.objects.create(
        total=5000,
        employer_contrib=2342,
        employee_contrib=2555,
        created_at=pytz.utc.localize(datetime.datetime(2017, 1, 1, 0, 0)),
        updated_at=pytz.utc.localize(datetime.datetime(2017, 1, 1, 0, 0)),
        user_id = fake_user.user_id
    )
    # look at application_controller.rb on how to set and authenticate the user and lookup based on user id
    # if user is NONE:
    #
    # retirement_info = user.retirement
    #
    # if they don't have retirement info set up, then create retirement
    t = get_template('users/retirement/index.html')
    html = t.render({'retirement': retirement_info})
    return HttpResponse(html)


@require_http_methods(["GET"])
def new_user_retirement(request, user_id):
    # user = (look up user ID in database)
    # retirement_info = Retirement.objects.create(
    #  total=0,
    #  employer_contrib=0,
    #  employee_contrib=0,
    #  created_at=pytz.utc.localize(datetime.datetime(2017, 1, 1, 0, 0)), dates??
    #  updated_at=pytz.utc.localize(datetime.datetime(2017, 1, 1, 0, 0)), dates??
    #  user_id = user
    # )
    return HttpResponse("New user retirement for user " + str(user))


@require_http_methods(["GET"])
def edit_user_retirement(request, user_id, retirement_id):
    return HttpResponse("Edit retirement " + str(retirement_id) +
                        " for user " + str(user))


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
def user_retirement(request, user_id, retirement_id):
    return HttpResponse("View retirement " + str(retirement_id) +
                        " for user " + str(user))

