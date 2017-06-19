from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client

import app.views.api.mobile.views as api_mobile_views
import app.views.api.users.views as api_users_views
import pytz
import datetime
from app.tests.mixins import RouteTestingWithKwargs
from django.urls import reverse
from app.models import User


class ApiMobileIndexTest(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        """ Class for testing api index view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:api_index'
        self.route = '/api/v1/mobile'
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
        self.kwargs = {}


class ApiMobileNewTest(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        """ Class for testing api index view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:api_new'
        self.route = '/api/v1/mobile/new'
        self.view = api_mobile_views.api_new
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


class ApiMobileEditTest(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        """ Class for testing api index view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:api_id_edit'
        self.route = '/api/v1/mobile/5/edit'
        self.view = api_mobile_views.api_id_edit
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
        self.kwargs = {'id_number': 5}


class ApiMobileIDTest(TestCase, RouteTestingWithKwargs):
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


class ApiUsersIndexTest(TestCase, RouteTestingWithKwargs):
    def setUp(self):
        """ Class for testing api index view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:api_users_index'
        self.route = '/api/v1/users'
        self.view = api_users_views.api_index
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


class ApiUsersByIDTest(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        """ Class for testing api index view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:api_users_id'
        self.route = '/api/v1/users/5'
        self.view = api_users_views.api
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

    def test_no_such_user_returns_empty_response(self):
        response = self.client.get(reverse(self.route_name, kwargs=self.kwargs))
        self.assertEquals(response.content, "[]")
