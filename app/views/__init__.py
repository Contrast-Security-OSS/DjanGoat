from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from dashboard import home as dashboard_home
from index import index as app_index
