# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pep8
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from app.tests.mixins import RouteTestingWithKwargs

import app.views as views

# import os
# cwd = os.getcwd()
# print(cwd)

dashboard = views.dashboard_views


class DashboardPep8Tests(TestCase):

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        path = 'app/views/dashboard/'
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([path + 'views.py',
                                        path + 'urls.py',
                                        path + '__init__.py'])
        error_message = ""
        if result.total_errors != 0:
            error_message = "Style errors in: " + path + "\n" + "\n".join(result.get_statistics())
        self.assertEqual(result.total_errors, 0, error_message)


# Tests checking that that '/dashboard' properly handles HttpRequests
# Accepts Both GET and POST requests and refuses all others with an error code 405 (Method not allowed)
class DashboardIndexHttpRequestMethodTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:dashboard_index'
        self.route = '/dashboard'
        self.view = dashboard.index
        self.responses = {
            'exists': 200,
            'GET': 200,
            'POST': 200,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {}


# Tests checking that that '/dashboard/home' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class DashboardHomeHttpRequestMethodTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:dashboard_home'
        self.route = '/dashboard/home'
        self.view = dashboard.home
        self.responses = {
            'exists': 200,
            'GET': 200,
            'POST': 405,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {}


# Tests checking that that '/dashboard/change_graph' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class DashboardChangeGraphHttpRequestMethodTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:dashboard_change_graph'
        self.route = '/dashboard/change_graph'
        self.view = dashboard.change_graph
        self.responses = {
            'exists': 200,
            'GET': 200,
            'POST': 405,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {}


# Tests checking that that '/dashboard/doc' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class DashboardDocHttpRequestMethodTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:dashboard_doc'
        self.route = '/dashboard/doc'
        self.view = dashboard.doc
        self.responses = {
            'exists': 200,
            'GET': 200,
            'POST': 405,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {}


# Tests checking that that '/dashboard/new' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class DashboardNewHttpRequestMethodTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:dashboard_new'
        self.route = '/dashboard/new'
        self.view = dashboard.new_dashboard
        self.responses = {
            'exists': 200,
            'GET': 200,
            'POST': 405,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {}


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
        self.responses = {
            'exists': 200,
            'GET': 200,
            'POST': 405,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {'dashboard_id': 55}


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
        self.responses = {
            'exists': 200,
            'GET': 200,
            'POST': 405,
            'PUT': 200,
            'PATCH': 200,
            'DELETE': 200,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {'dashboard_id': 55}
