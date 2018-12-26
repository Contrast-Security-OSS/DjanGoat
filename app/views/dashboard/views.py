from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from app.decorators import user_is_authenticated
from app.views import utils


@require_http_methods(["GET"])
@user_is_authenticated
def home(request):
    user = utils.current_user(request)
    context = user.__dict__
    try:
        income = user.work_info.first().income_to_int()
        pto_taken = int(user.pto.first().pto_taken)
        pto_remain = int(user.pto.first().pto_days_remaining())
        sick_taken = int(user.pto.first().sick_days_taken)
        sick_remain = int(user.pto.first().sick_days_remaining())
        performance = int(user.u_id.first().score)
        retirement = int(user.retirements.first().total)
        context.update({'income': income, 'pto_taken': pto_taken,
                        'pto_remain': pto_remain, 'sick_taken': sick_taken,
                        'sick_remain': sick_remain, 'performance': performance,
                        '401k': retirement})
    except:
        pass
    finally:
        context.update({'current_user': user})
    return render(request, 'dashboard/home.html', context=context)


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
@user_is_authenticated
def dashboard_view(request, dashboard_id):  # pylint: disable=unused-argument
    return HttpResponse("Dashboard " + str(dashboard_id))
