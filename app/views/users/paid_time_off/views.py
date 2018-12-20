from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from app.models import PaidTimeOff, Schedule
from django.utils import timezone
from django.contrib import messages
from app.decorators import user_is_authenticated
from app.views import utils


@require_http_methods(["GET", "POST"])
@user_is_authenticated
def index(request, user_id):
    user = utils.current_user(request)
    if not user:
        return HttpResponse("User " + str(user_id) + " NOT FOUND")
    pto = PaidTimeOff.objects.filter(user=user).first()
    if not pto:
        return HttpResponse("PTO " + str(user_id) + " NOT FOUND")
    if request.method == "GET":
        return index_get(request, user_id, user, pto)
    elif request.method == "POST":
        return index_post(request, user_id, user, pto)
    else:
        return HttpResponse("Invalid HTTP method")


def index_get(request, user_id, user, pto):  # pylint: disable=unused-argument
    schedules = Schedule.to_calendar((Schedule.objects.filter(pto=pto)))
    context = pto.__dict__
    context.update({"schedules": schedules, "current_user": user})
    return render(request, "users/paid_time_off.html",
                  context=context)


def index_post(request, user_id, user, pto):
    form = request.POST
    if not form:
        return HttpResponse("No form found")
    err_msg = PaidTimeOff.validate_PTO_form(form)
    if len(err_msg) > 0:
        messages.add_message(request, messages.INFO, err_msg)
    else:
        try:
            date_begin = Schedule.reformat(form['date_begin'])
            date_end = Schedule.reformat(form['date_end'])
            Schedule.objects.create(
                user=user, pto=pto, date_begin=date_begin,
                date_end=date_end, event_name=form['event_name'],
                event_type='PTO', event_desc=form['event_description'],
                created_at=timezone.now(), updated_at=timezone.now())
            messages.add_message(request, messages.INFO,
                                 "Information successfully updated")
        except Exception as e:
            messages.add_message(request, messages.INFO, str(e))
    url = "/users/%s/paid_time_off/" % user_id
    return redirect(url, permanent=False)
