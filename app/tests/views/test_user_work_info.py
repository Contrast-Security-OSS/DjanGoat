# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client
from django.urls import reverse

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
        self.kwargs = {'user_id': 55}
        self.expected_response_content = 'Work info index for user: 55'
        AuthRouteTestingWithKwargs.__init__(self)


# Tests checking that that '/users/:user_id/work_info/new' properly handles HttpRequests and routing
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserNewWorkInfoRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:new_user_work_info'
        self.route = '/users/55/work_info/new'
        self.view = work_info.new_user_work_info
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
        self.expected_response_content = 'New work info for user 55'
        AuthRouteTestingWithKwargs.__init__(self)


# Tests checking that that '/users/:user_id/work_info/:work_info_id/edit' properly handles HttpRequests and rout-
# ing
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# Tested on user_id 55 and work_info_id 22
class UserEditWorkInfoRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:edit_user_work_info'
        self.route = '/users/55/work_info/22/edit'
        self.view = work_info.edit_user_work_info
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
        self.kwargs = {'user_id': 55, 'work_info_id': 22}
        self.expected_response_content = 'Edit work info with id 22 for user 55'
        AuthRouteTestingWithKwargs.__init__(self)


# Tests checking that that '/users/:user_id/work_info/work_info_id' properly handles HttpRequests and routing
# Accepts GET, PATCH, PUT, and DELETE requests and refuses all others with an error code 405 (Method not allowed)
# Tested on user_id 55 and work_info_id 22
class UserShowWorkInfoRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:user_work_info'
        self.route = '/users/55/22'
        self.view = work_info.user_work_info
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
        self.kwargs = {'user_id': 55, 'work_info_id': 22}
        self.expected_response_content = 'View work info 22 for user 55'
        AuthRouteTestingWithKwargs.__init__(self)
