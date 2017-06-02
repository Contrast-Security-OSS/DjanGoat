from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET","POST"])
def home(request):
    return HttpResponse("DASHBOARD")
