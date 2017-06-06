# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from app.tests.mixins import RouteTestingMixin
from app.tests.mixins import RouteTestingWithKwargs

import app.views as views

users = views.users_views


# Tests checking that that '/users' properly handles HttpRequests
# Accepts Both GET and POST requests and refuses all others with an error code 405 (Method not allowed)
class UsersIndexRoutingAndHttpTests(TestCase, RouteTestingMixin):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:users_index'
        self.route = '/users'
        self.view = users.index
        self.responses = [200, 200, 405, 405, 405, 405, 405, 405]


# Tests checking that that '/users/new' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class UsersNewRoutingAndHttpTests(TestCase, RouteTestingMixin):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:users_new'
        self.route = '/users/new'
        self.view = users.new_user
        self.responses = [200, 405, 405, 405, 405, 405, 405, 405]


# Tests checking that that '/signup' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class UserSignupRoutingAndHttpTests(TestCase, RouteTestingMixin):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:user_signup'
        self.route = '/signup'
        self.view = users.signup
        self.responses = [200, 405, 405, 405, 405, 405, 405, 405]


# Tests checking that that '/users/:id/edit' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserEditRoutingAndHttpTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:user_edit'
        self.route = '/users/55/edit'
        self.view = users.edit_user
        self.responses = [200, 405, 405, 405, 405, 405, 405, 405]
        self.kwargs = {'user_id': 55}
        self.parameter = 55


# Tests checking that that '/users/:id/account_settings' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserAccountSettingsRoutingAndHttpTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:user_account_settings'
        self.route = '/users/55/account_settings'
        self.view = users.account_settings
        self.responses = [200, 405, 405, 405, 405, 405, 405, 405]
        self.kwargs = {'user_id': 55}
        self.parameter = 55


# Tests checking that that '/users/:id' properly handles HttpRequests
# Accepts GET, PATCH, PUT, and DELETE requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserViewRoutingAndHttpTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:user_view'
        self.route = '/users/55'
        self.view = users.user_view
        self.responses = [200, 405, 200, 200, 200, 405, 405, 405]
        self.kwargs = {'user_id': 55}
        self.parameter = 55
