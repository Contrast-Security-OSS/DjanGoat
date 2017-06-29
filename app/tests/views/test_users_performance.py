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
        self.expected_response_content = 'Performance History Visualization'
        AuthRouteTestingWithKwargs.__init__(self)
