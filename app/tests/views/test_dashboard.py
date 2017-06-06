# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from app.tests.mixins import RouteTestingMixin
from app.tests.mixins import RouteTestingWithKwargs

import app.views as views

dashboard = views.dashboard_views


# Tests checking that that '/dashboard' properly handles HttpRequests
# Accepts Both GET and POST requests and refuses all others with an error code 405 (Method not allowed)
class DashboardIndexHttpRequestMethodTests(TestCase, RouteTestingMixin):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:dashboard_index'
        self.route = '/dashboard'
        self.view = dashboard.index
        self.responses = [200, 200, 405, 405, 405, 405, 405, 405]


# Tests checking that that '/dashboard/home' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class DashboardHomeHttpRequestMethodTests(TestCase, RouteTestingMixin):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:dashboard_home'
        self.route = '/dashboard/home'
        self.view = dashboard.home
        self.responses = [200, 405, 405, 405, 405, 405, 405, 405]


# Tests checking that that '/dashboard/change_graph' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class DashboardChangeGraphHttpRequestMethodTests(TestCase, RouteTestingMixin):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:dashboard_change_graph'
        self.route = '/dashboard/change_graph'
        self.view = dashboard.change_graph
        self.responses = [200, 405, 405, 405, 405, 405, 405, 405]


# Tests checking that that '/dashboard/doc' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class DashboardDocHttpRequestMethodTests(TestCase, RouteTestingMixin):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:dashboard_doc'
        self.route = '/dashboard/doc'
        self.view = dashboard.doc
        self.responses = [200, 405, 405, 405, 405, 405, 405, 405]


# Tests checking that that '/dashboard/new' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class DashboardNewHttpRequestMethodTests(TestCase, RouteTestingMixin):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:dashboard_new'
        self.route = '/dashboard/new'
        self.view = dashboard.new_dashboard
        self.responses = [200, 405, 405, 405, 405, 405, 405, 405]


# Tests checking that that '/dashboard/:id/edit' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class DashboardEditHttpRequestMethodTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:dashboard_edit'
        self.route = '/dashboard/55/edit'
        self.view = dashboard.edit_dashboard
        self.responses = [200, 405, 405, 405, 405, 405, 405, 405]
        self.kwargs = {'dashboard_id': 55}
        self.parameter = 55


# Tests checking that that '/dashboard/:id' properly handles HttpRequests
# Accepts GET, PATCH, PUT, and DELETE requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class DashboardViewHttpRequestMethodTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:dashboard_view'
        self.route = '/dashboard/55'
        self.view = dashboard.dashboard_view
        self.responses = [200, 405, 200, 200, 200, 405, 405, 405]
        self.kwargs = {'dashboard_id': 55}
        self.parameter = 55
