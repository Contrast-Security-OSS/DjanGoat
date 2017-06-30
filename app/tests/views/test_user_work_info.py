# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase, RequestFactory, Client
from app.tests.mixins import AuthRouteTestingWithKwargs
from app.tests.mixins import Pep8ViewsTests
import app.views as views

work_info = views.user_work_info_views


class UserWorkInfoPep8Tests(TestCase, Pep8ViewsTests):
    def setUp(self):
        self.path = 'app/views/users/work_info/'


# Tests checking that that '/users/:user_id/work_info' properly handles HttpRequests and routing
# Accepts GET and POST requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserWorkInfoRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:user_work_info_index'
        self.route = '/users/55/work_info'
        self.view = work_info.user_work_info_index
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
        self.expected_response_content = 'Employee Information'
        AuthRouteTestingWithKwargs.__init__(self)
        self.kwargs = {'user_id': self.mixin_model.id}
