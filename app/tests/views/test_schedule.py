# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase, RequestFactory, Client
from app.tests.mixins import AuthRouteTestingWithKwargs
from app.tests.mixins import Pep8ViewsTests

import app.views as views

schedule = views.schedule_views


class SchedulePep8Tests(TestCase, Pep8ViewsTests):

    def setUp(self):
        self.path = 'app/views/schedule/'


# Tests checking that that '/schedule' properly handles HttpRequests and routing
# Accepts GET and POST requests and refuses all others with an error code 405 (Method not allowed)
class ScheduleIndexRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:schedule_index'
        self.route = '/schedule'
        self.view = schedule.schedule_index
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
        self.expected_response_content = 'Schedule index'
        AuthRouteTestingWithKwargs.__init__(self)


# Tests checking that that '/schedule/get_pto_schedule' properly handles HttpRequests and routing
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class PTOScheduleIndexRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:get_pto_schedule_schedule_index'
        self.route = '/schedule/get_pto_schedule'
        self.view = schedule.get_pto_schedule_schedule_index
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
        self.expected_response_content = 'PTO schedule index'
        AuthRouteTestingWithKwargs.__init__(self)


# Tests checking that that '/schedule/new' properly handles HttpRequests and routing
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class NewScheduleRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:new_schedule'
        self.route = '/schedule/new'
        self.view = schedule.new_schedule
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
        self.expected_response_content = 'New schedule'
        AuthRouteTestingWithKwargs.__init__(self)

# Tests checking that that '/schedule/:schedule_id/edit' properly handles HttpRequests and routing
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# Tested on schedule_id 55
class EditScheduleRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:edit_schedule'
        self.route = 'schedule/55/edit'
        self.view = schedule.edit_schedule
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
        self.kwargs = {'schedule_id': 55}
        self.expected_response_content = 'Edit schedule 55'
        AuthRouteTestingWithKwargs.__init__(self)


# Tests checking that that '/schedule/:schedule_id' properly handles HttpRequests and routing
# Accepts GET, PATCH, PUT, and DELETE requests and refuses all others with an error code 405 (Method not allowed)
# Tested on schedule_id 55
class UserShowRetirementRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:schedule'
        self.route = '/schedule/55'
        self.view = schedule.schedule
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
        self.kwargs = {'schedule_id': 55}
        self.expected_response_content = 'View schedule 55'
        AuthRouteTestingWithKwargs.__init__(self)
