from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from app.models import User, PaidTimeOff, Schedule
from django.utils import timezone
from django.contrib import messages


@require_http_methods(["GET", "POST"])
def index(request, user_id):
    user = User.objects.filter(user_id=user_id).first()
    if not user:
        return HttpResponse("User " + str(user_id) + " NOT FOUND")
    pto = PaidTimeOff.objects.filter(user=user).first()
    if not pto:
        return HttpResponse("PTO " + str(user_id) + " NOT FOUND")
    if request.method == "GET":
        schedules = Schedule.to_calendar((Schedule.objects.filter(pto=pto)))
        print(schedules)
        context = pto.__dict__
        context.update({"schedules": schedules})
        return render(request, "users/paid_time_off.html",
                      context=context)
    elif request.method == "POST":
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
                schedule = Schedule.objects.create(
                    user=user, pto=pto, date_begin=date_begin,
                    date_end=date_end, event_name=form['event_name'],
                    event_type='PTO', event_desc=form['event_description'],
                    created_at=timezone.now(), updated_at=timezone.now())
                messages.add_message(request, messages.INFO,
                                     "Information successfully updated")
            except Exception as e:
                messages.add_message(request, messages.INFO, str(e))
        url = "/users/%s/paid_time_off" % user_id
        return redirect(url, permanent=False)
    else:
        HttpResponse("Invalud HTTP method")


@require_http_methods(["GET"])
def new(request, user_id):
    return HttpResponse("You made a new pto for user " + str(user_id))


@require_http_methods(["GET"])
def edit(request, user_id, id):
    return HttpResponse("Edit PTO for user " + str(user_id) +
                        " with id " + str(id))


@require_http_methods(["GET", "PATCH", "DELETE", "PUT"])
def pto_id(request, user_id, id):
    return HttpResponse("Show, update, or destroy PTO for user " +
                        str(user_id) + " with id " + str(id))
