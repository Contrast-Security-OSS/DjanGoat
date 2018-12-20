from __future__ import unicode_literals

from django.template.loader import get_template
from django.http import HttpResponse


def index():
    t = get_template('index.html')
    html = t.render()
    return HttpResponse(html)