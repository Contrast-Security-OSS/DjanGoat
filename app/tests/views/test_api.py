from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client

import app.views.api.mobile.views as api_mobile_views
import app.views.api.users.views as api_users_views
from app.tests.mixins import AuthRouteTestingWithKwargs
from django.urls import reverse


class ApiMobileIndexTest(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        """ Class for testing api index view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:api_index'
        self.route = '/api/v1/mobile/1?class=user'
        self.view = api_mobile_views.api_index
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
        self.expected_response_content = 'hellohello'
        self.kwargs = {}


class ApiMobileIDTest(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        """ Class for testing api index view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:api_id'
        self.route = '/api/v1/mobile/5'
        self.view = api_mobile_views.api_id
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
        self.kwargs = {'id_number': 5}


class ApiUsersIndexTest(TestCase, AuthRouteTestingWithKwargs):
    def setUp(self):
        """ Class for testing api index view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:api_users_index'
        self.route = '/api/v1/users'
        self.view = api_users_views.api_index
        self.responses = {
            'exists': 401,
            'GET': 401,
            'POST': 405,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {}


class ApiUsersByIDTest(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        """ Class for testing api index view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:api_users_id'
        self.route = '/api/v1/users/5'
        self.view = api_users_views.api
        self.responses = {
            'exists': 401,
            'GET': 401,
            'POST': 405,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {'id_number': 5}
