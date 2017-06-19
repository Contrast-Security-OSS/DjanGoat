# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client
from app.tests.mixins import AuthRouteTestingWithKwargs
from app.tests.mixins import Pep8ViewsTests
import app.views as views

performance = views.user_performance_views


class PasswordResetPep8Tests(TestCase, Pep8ViewsTests):
    def setUp(self):
        self.path = 'app/views/users/performance/'


# /users/:user_id/performance(.:format) only accepts GET and POST
class UserPerformanceIndexRoutingTests(TestCase, AuthRouteTestingWithKwargs):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:user_performance_index'
        self.route = '/users/10/performance'
        self.view = performance.user_performance_index
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
        self.kwargs = {'user_id': 10}
        self.expected_response_content = 'Usr10performance index'
        AuthRouteTestingWithKwargs.__init__(self)


# /users/:user_id/performance/new(.:format) only accepts GET
class UserNewMessageRoutingTests(TestCase, AuthRouteTestingWithKwargs):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:new_user_performance'
        self.route = '/users/10/performance/new'
        self.view = performance.new_user_performance
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
        self.kwargs = {'user_id': 10}
        self.expected_response_content = 'New user performance for user 10'
        AuthRouteTestingWithKwargs.__init__(self)


# /users/:user_id/performance/:id/edit(.:format) only accepts GET
class UserEditPerformanceRoutingTests(TestCase, AuthRouteTestingWithKwargs):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:edit_user_performance'
        self.route = 'users/10/performance/20/edit'
        self.view = performance.edit_user_performance
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
        self.kwargs = {'user_id': 10, 'performance_id': 20}
        self.expected_response_content = 'Edit performance 20 for user 10'
        AuthRouteTestingWithKwargs.__init__(self)


# /users/:user_id/performance/:id(.:format) accepts GET, PATCH, PUT, DELETE
class UserShowPerformanceRoutingTests(TestCase, AuthRouteTestingWithKwargs):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:user_performance'
        self.route = '/users/10/performance/20'
        self.view = performance.user_performance
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
        self.kwargs = {'user_id': 10, 'performance_id': 20}
        self.expected_response_content = 'View performance 20 for user 10'
        AuthRouteTestingWithKwargs.__init__(self)
