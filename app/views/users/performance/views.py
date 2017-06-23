from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.template.loader import get_template
from app.views import utils
from app.decorators import user_is_authenticated


@require_http_methods(['GET', 'POST'])
@user_is_authenticated
def user_performance_index(request, user_id):
    current_user = utils.current_user(request)
    performance = current_user.u_id
    t = get_template('users/performance/index.html')
    html = t.render({'performance': performance,
                     'current_user': current_user})
    return HttpResponse(html)