# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client
from app.tests.mixins import RouteTestingWithKwargs
from app.tests.mixins import Pep8ViewsTests
import app.views as views

pto = views.pto_views


class PasswordResetPep8Tests(TestCase, Pep8ViewsTests):

    def setUp(self):
        self.path = 'app/views/users/paid_time_off/'


# Tests checking that that '/users/:user_id/paid_time_off' properly handles HttpRequests and routing
# Accepts GET and POST requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserPTOIndexRoutingAndHttpTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:pto_index'
        self.route = '/users/55/paid_time_off'
        self.view = pto.index
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
        self.kwargs = {'user_id': 55}


# Tests checking that that '/users/:user_id/retirement/new' properly handles HttpRequests and routing
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class PTONewRoutingAndHttpTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:pto_new'
        self.route = '/users/55/retirement/new'
        self.view = pto.new
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
        self.kwargs = {'user_id': 55}


# Tests checking that that '/users/:user_id/retirement/:retirement_id/edit' properly handles HttpRequests and routing
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# Tested on user_id 55 and retirement_id 22
class PTOEditRoutingAndHttpTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:pto_edit'
        self.route = 'users/55/paid_time_off/22/edit'
        self.view = pto.edit
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
        self.kwargs = {'user_id': 55, 'id': 22}


# Tests checking that that '/users/:user_id/retirement/:retirement_id' properly handles HttpRequests and routing
# Accepts GET, PATCH, PUT, and DELETE requests and refuses all others with an error code 405 (Method not allowed)
# Tested on user_id 55 and retirement_id 22
class UserShowRetirementRoutingAndHttpTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:pto_id'
        self.route = '/users/55/paid_time_off/22'
        self.view = pto.pto_id
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
        self.kwargs = {'user_id': 55, 'id': 22}
