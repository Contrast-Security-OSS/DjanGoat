# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client
from app.tests.mixins import RouteTestingWithKwargs

import app.views as views

# print(views.users_views)
retirement = views.user_retirement_views


# Tests checking that that '/users/:user_id/retirement' properly handles HttpRequests and routing
# Accepts GET and POST requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserRetirementIndexRoutingAndHttpTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:user_retirement_index'
        self.route = '/users/55/retirement'
        self.view = retirement.user_retirement_index
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
class UserNewMessageRoutingAndHttpTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:new_user_retirement'
        self.route = '/users/55/retirement/new'
        self.view = retirement.new_user_retirement
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
class UserEditRetirementRoutingAndHttpTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:edit_user_retirement'
        self.route = 'users/55/retirement/22/edit'
        self.view = retirement.edit_user_retirement
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
        self.kwargs = {'user_id': 55, 'retirement_id': 22}


# Tests checking that that '/users/:user_id/retirement/:retirement_id' properly handles HttpRequests and routing
# Accepts GET, PATCH, PUT, and DELETE requests and refuses all others with an error code 405 (Method not allowed)
# Tested on user_id 55 and retirement_id 22
class UserShowRetirementRoutingAndHttpTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:user_retirement'
        self.route = '/users/55/retirement/22'
        self.view = retirement.user_retirement
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
        self.kwargs = {'user_id': 55, 'retirement_id': 22}
