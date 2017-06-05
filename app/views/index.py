from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

def index(request):
    return HttpResponse("Hello, world. You're at the app index.")
