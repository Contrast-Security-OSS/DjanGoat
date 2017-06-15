from __future__ import unicode_literals

from django.template.loader import get_template
from django.http import HttpResponse


def index(request):
    auth_token = request.COOKIES['auth_token']

    if auth_token is not None:
        return HttpResponse("<h1>" + auth_token + "</h1>")
    else:
        t = get_template('index.html')
        html = t.render()
        return HttpResponse(html)