from __future__ import unicode_literals
from django.test import TestCase, RequestFactory, Client
from app.tests.mixins import RouteTestingWithKwargs
import app.views.api.views as api_views


class ApiIndexTest(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        """ Class for testing api index view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:api_index'
        self.route = '/api/v1/mobile'
        self.view = api_views.api_index
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


class ApiNewTest(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        """ Class for testing api index view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:api_new'
        self.route = '/api/v1/mobile/new'
        self.view = api_views.api_new
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


class ApiEditTest(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        """ Class for testing api index view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:api_id_edit'
        self.route = '/api/v1/mobile/5/edit'
        self.view = api_views.api_id_edit
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


class ApiIDTest(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        """ Class for testing api index view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:api_id'
        self.route = '/api/v1/mobile/5'
        self.view = api_views.api_id
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