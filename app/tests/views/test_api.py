from __future__ import unicode_literals
from django.test import TestCase, RequestFactory, Client
from app.tests.mixins import RouteTestingWithKwargs
import app.views.api.views as api_views


class ApiIndexTest(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
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