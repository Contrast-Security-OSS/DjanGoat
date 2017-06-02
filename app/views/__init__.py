from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from dashboard import home as dashboard_home
from dashboard import doc as dashboard_doc
from dashboard import index as dashboard_index
from dashboard import change_graph as dashboard_change_graph
from dashboard import new_dashboard as dashboard_new
from dashboard import edit_dashboard as dashboard_edit
from dashboard import dashboard as dashboard

from index import index as app_index
